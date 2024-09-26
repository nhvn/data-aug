from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Data Augmentation API"

# Route for uploading and processing images
@app.route('/upload', methods=['POST'])
def upload_image():
    # Check if a file is present in the request
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    # Get the uploaded file
    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # You can now process the file (apply augmentations, etc.)
    # For now, we'll just return a success message
    return jsonify({"message": f"File '{file.filename}' uploaded and processed!"})

if __name__ == '__main__':
    app.run(debug=True)
