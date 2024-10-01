import sys
import os
from flask import Flask, request, send_file, jsonify
import io
import zipfile
from PIL import Image

# Add the src directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.append(src_dir)

from gan_handler import GANHandler

app = Flask(__name__, static_folder='../frontend/static', template_folder='templates')

# Initialize the GAN Handler
gan_handler = GANHandler()
gan_handler.initialize(None)  # Pass None as context for now

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hackathon')
def hackathon_page():
    return render_template('hackathon.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    if 'files[]' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    files = request.files.getlist('files[]')
    
    if not files or files[0].filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    generated_images = []
    for _ in files:  # We don't need the uploaded file, just generate based on the count
        try:
            # Generate a new image using the GAN
            generated_image_bytes = gan_handler.handle(None, None)
            generated_images.append(generated_image_bytes)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    if len(generated_images) == 1:
        # If only one image, send it directly
        return send_file(
            io.BytesIO(generated_images[0]),
            mimetype='image/png',
            as_attachment=True,
            download_name='generated_image.png'
        )
    else:
        # If multiple images, create a zip file
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
    app.run(debug=True)