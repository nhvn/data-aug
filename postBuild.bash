#!/bin/bash
# Post-build setup script for AI Workbench

# Install Python dependencies
pip install -r requirements.txt

# Setup application directories
mkdir -p backend/outputs/models
mkdir -p backend/data/uploads
mkdir -p frontend/static

# Set permissions
chmod -R 755 backend
chmod -R 755 frontend

echo "Post-build setup completed successfully"
