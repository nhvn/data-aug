import os
from pathlib import Path

# Base paths for AI Workbench
WORKSPACE_DIR = Path('/workspace')
BACKEND_DIR = WORKSPACE_DIR / 'backend'

# Directory structure
DATA_DIR = BACKEND_DIR / 'data'
MODELS_DIR = BACKEND_DIR / 'outputs/models'
OUTPUTS_DIR = BACKEND_DIR / 'outputs/generated_images'
UPLOAD_DIR = DATA_DIR / 'uploads'

# Create all required directories
for dir_path in [DATA_DIR, MODELS_DIR, OUTPUTS_DIR, UPLOAD_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

# Model configuration
BATCH_SIZE = 32
IMAGE_SIZE = 64
CHANNELS = 3
LATENT_DIM = 100

# Flask configuration
FLASK_ENV = os.getenv('FLASK_ENV', 'development')
DEBUG = FLASK_ENV == 'development'
HOST = '0.0.0.0'
PORT = 5000

# Model paths
GENERATOR_PATH = MODELS_DIR / 'generator_final.pt'
DISCRIMINATOR_PATH = MODELS_DIR / 'discriminator_final.pt'