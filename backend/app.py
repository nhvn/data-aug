from flask import Flask, request, jsonify, render_template
from PIL import Image
import os

# Create the Flask app
app = Flask(__name__)

# Ensure the uploads directory exists
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# Home route
@app.route('/')
def home():
    return "Welcome to the Data Augmentation API"

# Route for the image upload form page
@app.route('/upload-image')
def upload_image_page():
    return render_template('upload.html')  # Renders the HTML form

# Route for handling the image upload and processing
@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['file']
    if file:
        filename = file.filename
        filepath = os.path.join("uploads", filename)
        
        # Save the uploaded image to the 'uploads' directory
        file.save(filepath)
        
        # Open the image and apply augmentations (e.g., resizing)
        img = Image.open(filepath)
        img = img.resize((256, 256))  # Example augmentation: resize image to 256x256
        img.save(filepath)  # Save the augmented image back to the file

        # Return a success message with the filename
        return jsonify({"message": "Image uploaded and augmented!", "file": filename})
    return jsonify({"error": "No file uploaded"}), 400

if __name__ == '__main__':
    app.run(debug=True)
