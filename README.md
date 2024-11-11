# AugmentAI - Data Augmentation Tool

This project provides an image augmentation tool using **Generative AI** models, specifically designed and optimized for **NVIDIA AI Workbench**. It leverages GPU acceleration for efficient data augmentation and synthetic image generation.

---

## Description

AugmentAI allows users to upload image datasets and augment them using generative models. The system uses Stability AI API for high-quality image generation and falls back to a local GAN model when needed. Built specifically for **NVIDIA AI Workbench**, the application utilizes GPU acceleration for fast and efficient image processing.

---

## Features

- **Infrastructure**
  - Built specifically for NVIDIA AI Workbench
  - Easy deployment and management
  - No complex setup needed

- **User Experience**
  - Simple, clean interface
  - Folder upload support
  - Maintains original image dimensions
  - Direct result downloads

- **Future Potential**
  - Framework ready for multi-modal expansion
  - Could integrate multiple AI models
  - Potential for text and tabular data support

---

## Image Generation Approaches

This project implements two approaches for image generation:

### 1. Primary Service (Stability AI API)
- High-quality image generation
- Maintains original image dimensions
- Production-ready results
- Faster inference times

### 2. Fallback Service (Local GAN)
- Custom GAN model trained on nature dataset
- 64x64 pixel output
- CPU-based inference
- Automatically activated if API is unavailable

---

## Installation & Setup

### Prerequisites
- NVIDIA AI Workbench installed and configured
- Docker Desktop running
- Git installed

### Steps
1. Open NVIDIA AI Workbench
- Select "Clone Project"
```bash
    https://github.com/nhvn/data-aug.git

- Click on "Clone"

2. Start the Application:
- In Workbench, go to Environment > Applications
- Click on AugmentAI to launch the application
- The application will open automatically in your default browser

---

## Accessing the Application

- The application is avaliable at: http://localhost:10000/projects/data-aug/applications/AugmentAI/

---

## Using the Application

1. Launch through NVIDIA AI Workbench
2. Navigate to the "Upload" page or click on 'Augment' in the navigation bar
3. Upload images (folder or individual files)
4. Click 'Augment' to generate variations and download generated images

---

## Limitations and Guidelines

- Supported formats: PNG, JPG, JPEG
- Maximum 10 files per upload
- Maximum total upload size: 16MB
- Maximum image dimensions: 1024x1024 pixels (larger images automatically resized)
- Folder and file drag-and-drop supported
- Upload status indication provided

---

## Troubleshooting

If you encounter issues:
1. Ensure Docker Desktop is running
2. Verify NVIDIA AI Workbench is properly installed
3. Check the application logs in Workbench
4. Ensure your API key is properly configured (if using Stability AI)
5. Try restarting the application through Workbench

---

## Development Notes

This project is specifically designed for NVIDIA AI Workbench. Key configurations include:
- NVIDIA AI Workbench integration
- Stability AI API integration
- Local GAN model fallback
- Static file serving optimization
 
---

## Contact

If you're a judge and need access or have questions, please reach out and I will respond as soon as possible.
 
---

## Blog Post

Read the full blog post [here](./blogpost.md).
