#!/bin/bash
# Pre-build setup script for AI Workbench

# Change to the project directory
cd /project

# Use sudo for directory creation
sudo mkdir -p backend/src
sudo mkdir -p backend/templates
sudo mkdir -p frontend/static

# Set correct permissions
sudo chown -R workbench:workbench /project

# Check for required files
if [ ! -f "requirements.txt" ]; then
    echo "Creating requirements.txt"
    cat > requirements.txt << EOF
flask==3.0.3
pillow==10.4.0
torch>=2.2.0
torchvision>=0.17.0
matplotlib==3.7.1
numpy<2
EOF
fi

echo "Pre-build setup completed successfully"
