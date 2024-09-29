from flask import Flask, request, render_template, jsonify, send_file
from PIL import Image
import os
import io
import zipfile
import random

app = Flask(__name__, static_folder='../frontend/static', template_folder='templates')

UPLOAD_FOLDER = 'uploads'
AUGMENTED_FOLDER = 'augmented'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUGMENTED_FOLDER, exist_ok=True)

def augment_image(img):
    # Perform basic augmentations (you can add more sophisticated augmentations here)
    augmentations = [
        lambda x: x.rotate(random.randint(-30, 30)),
        lambda x: x.transpose(Image.FLIP_LEFT_RIGHT),
        lambda x: x.transpose(Image.FLIP_TOP_BOTTOM),
    ]
    return random.choice(augmentations)(img)

@app.route('/')
@app.route('/upload-image')
def upload_image_page():
    return render_template('upload.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'GET':
        return render_template('upload.html')
    
    if 'files[]' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    files = request.files.getlist('files[]')
    
    if not files or files[0].filename == '':
        return jsonify({"error": "No selected file"}), 400

    augmented_files = []
    for file in files:
        if file and file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            filename = file.filename
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            # Open the image and apply augmentations
            img = Image.open(filepath)
            augmented_img = augment_image(img)
            augmented_filename = f"augmented_{filename}"
            augmented_filepath = os.path.join(AUGMENTED_FOLDER, augmented_filename)
            augmented_img.save(augmented_filepath)
            augmented_files.append(augmented_filepath)

    # Create a ZIP file containing all augmented images
    memory_file = io.BytesIO()
    with zipfile.ZipFile(memory_file, 'w') as zf:
        for file in augmented_files:
            zf.write(file, os.path.basename(file))
    memory_file.seek(0)

    return send_file(
        memory_file,
        mimetype='application/zip',
        as_attachment=True,
        download_name='augmented_images.zip'
    )

if __name__ == '__main__':
    app.run(debug=True)