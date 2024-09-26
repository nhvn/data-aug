# Generative AI Data Augmentation Tool

This project provides a tool for augmenting datasets using **Generative AI** models to enhance machine learning workflows. By leveraging **NVIDIA AI Workbench**, it ensures efficient model training, management, and deployment, offering users the ability to generate synthetic data and apply various augmentation techniques.

---

## Description

Users can upload datasets (images, text, or tabular data) and augment them using generative models. The system uses pre-trained **Generative AI** models (like GANs, transformers, and CTGANs) to create synthetic data that can improve the performance of machine learning models. The integration with **NVIDIA AI Workbench** optimizes the workflow by utilizing GPU acceleration for fast and scalable model training and deployment.

---

## Features

- **Upload Dataset**: Users can upload images, text, or tabular data for augmentation.
- **Data Augmentation**: Apply various augmentation techniques (e.g., image transformations, synthetic text generation, and tabular data enhancement).
- **Synthetic Data Generation**: Utilize pre-trained Generative AI models to generate realistic synthetic data.
- **Data Export**: Augmented data can be downloaded or accessed via API for integration into machine learning pipelines.

---

## Core Functionalities

1. **Dataset Upload**: Support for different data formats (image, text, and tabular).
2. **Augmentation Selection**: Choose from various augmentation techniques based on the data type.
3. **Synthetic Data Generation**: Realistic synthetic data generation using AI models such as:
    - **GANs (Generative Adversarial Networks)** for image generation.
    - **Transformers** for text data augmentation.
    - **CTGAN** for tabular data synthesis.
4. **Integration with NVIDIA AI Workbench**:
    - **Model Training**: Utilize AI Workbench for accelerated training.
    - **Deployment**: Seamless model deployment for real-time inference.
    - **Workflow Automation**: Automated workflows for managing model pipelines.

---

<!-- ## Project Structure
data-aug/
├── backend/                  # Backend API services and model logic (Flask)
│   ├── app.py                # Main Flask application
│   ├── templates/            # HTML templates for the web interface
│   ├── uploads/              # Folder for storing uploaded/augmented files
│   ├── model_store/          # TorchServe models (.mar files)
│   └── static/               # Static assets (CSS/JS if needed)
├── frontend/                 # Frontend (React, Vue.js, or simple HTML/CSS)
├── models/                   # Pre-trained generative models (GANs, transformers, CTGAN)
├── scripts/                  # Utility scripts for NVIDIA AI Workbench, training, etc.
├── new_venv/                 # Python virtual environment folder
├── README.md                 # Project documentation (this file)
├── requirements.txt          # Backend dependencies
├── config.properties         # TorchServe configuration file
└── .gitignore                # Ignored files for Git -->


## Installation
- Prerequisites
NVIDIA AI Workbench installed and configured.
Docker (optional, for containerized development).
Python 3.8+ with pip installed.

- Steps

1. Clone the repository:
git clone https://github.com/YourUsername/GenerativeAI-DataAugmentation.git
cd GenerativeAI-DataAugmentation

2. Create and activate a virtual environment:
python3 -m venv new_venv
source new_venv/bin/activate
- For Windows: new_venv\Scripts\activate

3. Install the dependencies:
pip install -r requirements.txt

4. Set up NVIDIA AI Workbench:
Follow the NVIDIA AI Workbench installation guide.
Configure the environment for generative models (GANs, transformers, CTGAN).

5. Start the backend server:
python3 backend/app.py

6. Access the web interface:
Open a browser and go to http://127.0.0.1:5000/upload-image to upload your dataset.

7. Usage & NVIDIA AI Workbench Integration
Once the project is set up:

- Upload Dataset: Users can upload datasets via the web interface for images. (text and tabular coming later).
<!-- Select Augmentation Options: Choose from various augmentation techniques based on the data type.
Generate Synthetic Data: Synthetic data is generated using pre-trained AI models, such as: -->

- GANs (Generative Adversarial Networks) for image generation.
<!-- Transformers for text data generation.
CTGAN for tabular data augmentation. -->


8. Download Augmented Data: The augmented dataset can be downloaded or accessed through an API for use in machine learning models.

---

## NVIDIA AI Workbench Integration

- Training: The core models (GAN, transformers, CTGAN) are trained with the help of NVIDIA AI Workbench, utilizing GPU acceleration to reduce training time and enhance performance.
- Deployment: Once trained, the models are packaged and deployed using TorchServe for real-time inference.
- Inference: The backend uses these models to process real-time requests for data augmentation and synthetic data generation.
- Workflow Automation: NVIDIA AI Workbench facilitates workflow management, automating the process of retraining and redeploying models as new data becomes available, ensuring optimal productivity and scalability.

---

## Example Workflow

- Image Augmentation:
A user uploads an image via the web interface.
The backend applies augmentations (like rotation, flipping, resizing) using the generative model.
The augmented image is saved to the uploads folder and available for download.


<!-- Text Augmentation:
A user uploads a text dataset.
The backend uses a pre-trained transformer model to generate synthetic text based on the input data.
The augmented text is processed and returned to the user for download.


Tabular Data Augmentation:
A user uploads tabular data.
The backend uses CTGAN (Conditional Tabular GAN) to generate new synthetic rows of data based on the uploaded dataset.
The augmented dataset is provided for download. -->

---

## Roadmap

- Basic Functionality:
Implement image augmentation (rotation, flipping, resizing) using pre-trained GAN models.
Add support for text data augmentation using transformer models.
Enable augmentation for tabular data using CTGAN.

- Frontend Enhancements:
Build a more comprehensive user interface to support dataset uploads and augmentation selection.

- Advanced Features:
Integrate more advanced augmentation techniques for all data types.
Enable users to visualize and compare the original and augmented data.
Automate model retraining workflows using NVIDIA AI Workbench.

- Deployment:
Scale the backend to handle multiple users and datasets.
Ensure seamless deployment using TorchServe integrated with NVIDIA AI Workbench for GPU-accelerated inference.