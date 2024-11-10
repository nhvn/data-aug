import sys
import os
from pathlib import Path
from flask import Flask, request, send_file, jsonify, render_template, url_for, redirect
import io
import zipfile
from PIL import Image
from src.image_handler import ImageHandler

# Force Python to flush prints immediately
import sys
sys.stdout.flush()

# Debug information
with open('/project/debug.log', 'w') as f:
    f.write("=== Debug Directory Information ===\n")
    f.write(f"Current directory: {os.getcwd()}\n")
    
    # Workbench project structure
    PROJECT_DIR = Path('/project')
    f.write(f"PROJECT_DIR: {PROJECT_DIR}\n")
    
    BACKEND_DIR = PROJECT_DIR / 'backend'
    SRC_DIR = BACKEND_DIR / 'src'
    STATIC_DIR = PROJECT_DIR / 'frontend/static'
    f.write(f"STATIC_DIR path: {STATIC_DIR}\n")
    f.write(f"STATIC_DIR exists: {STATIC_DIR.exists()}\n")
    
    if STATIC_DIR.exists():
        f.write(f"STATIC_DIR contents: {list(STATIC_DIR.iterdir())}\n")
        images_dir = STATIC_DIR / 'images'
        f.write(f"Images directory exists: {images_dir.exists()}\n")
        if images_dir.exists():
            f.write(f"Images directory contents: {list(images_dir.iterdir())}\n")
    
    f.write("================================\n")

# Workbench project structure
PROJECT_DIR = Path('/project')
BACKEND_DIR = PROJECT_DIR / 'backend'
SRC_DIR = BACKEND_DIR / 'src'
STATIC_DIR = PROJECT_DIR / 'frontend/static'
TEMPLATE_DIR = BACKEND_DIR / 'templates'
MODEL_DIR = BACKEND_DIR / 'outputs/models'

# Ensure critical directories exist
for d in [SRC_DIR, STATIC_DIR, TEMPLATE_DIR, MODEL_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# Add source directory to path
sys.path.append(str(SRC_DIR))

try:
    from src.gan_handler import GANHandler
except ImportError as e:
    print(f"Error importing GANHandler: {e}")
    sys.exit(1)

# Initialize Flask
app = Flask(
    __name__,
    static_folder=str(STATIC_DIR),
    template_folder=str(TEMPLATE_DIR)
)

# Configure Flask
app.config.update(
    MAX_CONTENT_LENGTH=16 * 1024 * 1024,  # 16MB max file size
    MODEL_PATH=str(MODEL_DIR / 'generator_final.pt'),
    APPLICATION_ROOT='/projects/data-aug/applications/AugmentAI',
    SEND_FILE_MAX_AGE_DEFAULT=0,
    STATIC_URL_PATH='/projects/data-aug/applications/AugmentAI/static'
)

# Initialize GAN Handler
try:
    gan_handler = GANHandler()
    gan_handler.initialize(None)
except Exception as e:
    print(f"Error initializing GAN Handler: {e}")
    sys.exit(1)

# Custom static route to handle MIME types
@app.route('/projects/data-aug/applications/AugmentAI/static/<path:filename>')
def custom_static(filename):
    mimetype = None
    if filename.endswith('.css'):
        mimetype = 'text/css'
    elif filename.endswith('.js'):
        mimetype = 'application/javascript'
    elif filename.endswith('.png'):
        mimetype = 'image/png'
    return send_file(os.path.join(STATIC_DIR, filename), mimetype=mimetype)

# Health check endpoint
@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

# Keep the routes simple
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/hackathon')
def hackathon_page():
    return render_template('hackathon.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        return redirect(url_for('generate_image', _external=True, _scheme='http'))
    return render_template('upload.html')

# Initialize handler
image_handler = ImageHandler(use_api=True)  # Set to False for GAN

@app.route('/generate', methods=['POST'])
def generate_image():
    if 'files[]' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    files = request.files.getlist('files[]')
    MAX_FILES = 10
    
    if len(files) > MAX_FILES:
        return jsonify({"error": f"Maximum {MAX_FILES} files allowed"}), 400
    
    if not files or files[0].filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    generated_images = []
    
    for file in files:
        if file and file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                uploaded_image = Image.open(file)
                # In your app.py, update this line:
                generated_image_bytes = image_handler.generate_from_image(uploaded_image)  # Changed from generate_image
                generated_images.append(generated_image_bytes)
            except Exception as e:
                return jsonify({"error": str(e)}), 500
    
    if len(generated_images) == 1:
        return send_file(
            io.BytesIO(generated_images[0]),
            mimetype='image/png',
            as_attachment=True,
            download_name='generated_image.png'
        )
    else:
        memory_file = io.BytesIO()
        with zipfile.ZipFile(memory_file, 'w') as zf:
            for i, img_bytes in enumerate(generated_images):
                zf.writestr(f'generated_image_{i+1}.png', img_bytes)
        memory_file.seek(0)
        
        return send_file(
            memory_file,
            mimetype='application/zip',
            as_attachment=True,
            download_name='generated_images.zip'
        )

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
