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

Steps

1. Clone the repository:
git clone https://github.com/nhvn/data-aug.git
cd GenerativeAI-DataAugmentation

2. Create and activate a virtual environment:
python3 -m venv new_venv
source new_venv/bin/activate
- For Windows: new_venv\Scripts\activate

3. Install the dependencies:
pip install -r requirements.txt

4. Configure NVIDIA AI Workbench:
Follow the NVIDIA AI Workbench installation guide below.
Configure the environment for generative models (GANs, transformers, CTGAN).

5. Start the backend server:
python3 backend/app.py

6. Access the web interface:
Open a browser and go to http://127.0.0.1:5000/ to upload your dataset (or an image for demonstration purposes).

7. Usage & NVIDIA AI Workbench Integration
Once the project is set up:

- Upload Dataset: Users can upload datasets via the web interface for images. (text and tabular coming later).
<!-- Select Augmentation Options: Choose from various augmentation techniques based on the data type.
Generate Synthetic Data: Synthetic data is generated using pre-trained AI models, such as: -->

- GANs (Generative Adversarial Networks) for image generation.
<!-- Transformers for text data generation.
CTGAN for tabular data augmentation. -->


8. Download Augmented Data: The augmented dataset can be downloaded through the browser.

---

## NVIDIA AI Workbench Integration

- Training: The core models (GAN, transformers, CTGAN) are trained with the help of NVIDIA AI Workbench, utilizing GPU acceleration to reduce training time and enhance performance.
- Deployment: Once trained, the models are packaged and deployed using TorchServe for real-time inference.
- Inference: The backend uses these models to process real-time requests for data augmentation and synthetic data generation.
- Workflow Automation: NVIDIA AI Workbench facilitates workflow management, automating the process of retraining and redeploying models as new data becomes available, ensuring optimal productivity and scalability.

---

## How to Work with NVIDIA AI Workbench

Prerequisites
- Install NVIDIA AI Workbench by following the official installation guide.
- Ensure you have access to a system with a compatible NVIDIA GPU.

Setting Up NVIDIA AI Workbench for This Project
1. Clone the Repository:
git clone https://github.com/nhvn/data-aug.git
cd GenerativeAI-DataAugmentation

2. Create and Activate a Virtual Environment:
python3 -m venv new_venv
source new_venv/bin/activate
# On Windows, use: new_venv\Scripts\activate

3. Install Project Dependencies:
pip install -r requirements.txt

4. Configure NVIDIA AI Workbench:
To run your project using NVIDIA AI Workbench, configure the workbench environment by setting up the necessary models (GANs, transformers, CTGAN) within the Workbench platform.
- In your NVIDIA AI Workbench instance, create a new project.
- Upload the project files from this repository.
- Make sure to configure the Workbench environment with GPU resources to accelerate model training.

5. Run Training with NVIDIA AI Workbench:
Execute model training using GPU acceleration:
- Within the NVIDIA AI Workbench, navigate to your project’s directory and select the GAN, Transformer, or CTGAN model you want to train.
- Start the training process by selecting the appropriate model configuration and allocating GPU resources.

6. Deploy the Trained Model with TorchServe:
- Package the trained model into a .mar file.
- Start TorchServe to handle real-time inference using the trained model.
torchserve --start --model-store model_store --models my_model.mar

7. Inference and Workflow Automation:

The backend Flask API will automatically make use of the trained models for augmentation tasks.
Users can upload datasets via the web interface, and NVIDIA AI Workbench facilitates workflow automation to streamline retraining and redeploying models as new data is introduced.

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

## Acknowledged Limitations

Due to hardware limitations, the current version of AugmentAI has been developed and demonstrated using CPU resources, which impacts training time and overall model performance. However, the project is designed to fully support GPU acceleration through NVIDIA AI Workbench.

---

## Roadmap

- Basic Functionality:
Implement image augmentation (rotation, flipping, resizing) using pre-trained GAN models.
Add support for text data augmentation using transformer models.
Enable augmentation for tabular data using CTGAN.

- Frontend Enhancements:
Build a more comprehensive user interface to support dataset uploads and augmentation selection.

- Planned Improvements:
Advanced Augmentation Techniques: AugmentAI will continue to evolve by integrating more advanced techniques to offer users greater control over the augmentation process.
Text Data Augmentation: Future updates will introduce synthetic text generation using transformer models to augment text datasets, enhancing machine learning workflows for natural language processing tasks.
Tabular Data Augmentation: Planned integration with CTGAN will enable synthetic tabular data generation, useful for tasks like predictive modeling and data imbalance correction.

- Deployment:
Scale the backend to handle multiple users and datasets.
Ensure seamless deployment using TorchServe integrated with NVIDIA AI Workbench for GPU-accelerated inference.

## Blog Post
Read the full blog post [here](./blogpost.md).
