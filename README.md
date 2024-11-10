# AugmentAI - Data Augmentation Tool

This project provides an image augmentation tool using **Generative AI** models, specifically designed and optimized for **NVIDIA AI Workbench**. It leverages GPU acceleration for efficient data augmentation and synthetic image generation.

---

## Description

AugmentAI allows users to upload image datasets and augment them using generative models. The system uses pre-trained **Generative AI** models (GANs) to generate synthetic images that can enhance machine learning model performance. Built specifically for **NVIDIA AI Workbench**, the application utilizes GPU acceleration for fast and efficient image processing.

---

## Features

- **Image Upload**: Upload folders of images for augmentation
- **Data Augmentation**: Generate synthetic variations of uploaded images using GANs
- **GPU Acceleration**: Utilize NVIDIA AI Workbench's GPU capabilities
- **Web Interface**: User-friendly interface for easy interaction
- **Instant Download**: Augmented images available for immediate download

---

<!-- ## Project Structure
data-aug/
├── backend/
│   ├── src/
│   │   └── gan_handler.py
│   ├── templates/
│   └── app.py
├── frontend/
│   └── static/
│       ├── images/
│       ├── js/
│       └── styles.css
├── models/
├── .project/
│   └── spec.yaml
└── README.md -->

## Prerequisites

- NVIDIA AI Workbench installed and configured
- Docker Desktop running
- Git installed

---

## Installation & Setup

1. Clone the repository:
- ```bash
- git clone https://github.com/nhvn/data-aug.git
- cd data-aug

2. Open in NVIDIA AI Workbench:
- Launch NVIDIA AI Workbench
- Select "Open Project"
- Navigate to the cloned data-aug directory
- The project will automatically configure the necessary environment

3. Start the Application:
- In Workbench, go to Environment > Applications
- Click on AugmentAI to launch the application
- The application will open automatically in your default browser

---

## Accessing the Application

- The application is avaliable at: http://localhost:10000/projects/data-aug/applications/AugmentAI/

## NVIDIA AI Workbench Integration

- Environment Management: Workbench handles all environment setup and dependencies
- GPU Acceleration: Automatic GPU utilization for model inference
- Application Deployment: Seamless deployment through Workbench's application management
- Resource Management: Efficient handling of GPU and memory resources

---

## Using the Application

1. Launch the application through NVIDIA AI Workbench
2. Click "Augment" in the navigation bar
3. Upload a folder of images (3-5 images recommended)
4. Click 'Augment' to generate synthetic variations
5. Download the augmented images

---

## Known Limitations

- Currently supports folder upload only (single image upload coming soon)
- File drag-and-drop functionality is under development
- Upload status indicator is in development

---

## Future Enhancements

- Single image upload support
- Drag-and-drop functionality
- Upload progress indicator
- Additional augmentation options
- Enhanced GPU optimization
- Batch processing improvements

---

## Development Notes

This project is specifically designed for NVIDIA AI Workbench. Key configurations include:
- spec.yaml configuration for Workbench integration
- PU resource allocation
- Application routing through Workbench proxy
- Static file serving optimization

---

## Troubleshooting

If you encounter issues:
1. Ensure Docker Desktop is running
2. Verify NVIDIA AI Workbench is properly installed
3. Check the application logs in Workbench
4. Ensure your GPU drivers are up to date
5. Try restarting the application through Workbench

---

## Contact

If you're a judge and need access or have questions, please reach out.
 
---

## Blog Post

Read the full blog post [here](./blogpost.md).