import os
import torch
from gan_models import Generator
from torchvision import transforms
from PIL import Image
import io

class GANHandler:
    def __init__(self):
        self.z_dim = 100  # Latent space dimension
        self.img_size = 64  # New image size
        self.channels = 3  # RGB channels

    def initialize(self, context):
        # Set the device (use GPU if available)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # Initialize the Generator model and load weights
        self.model = Generator(self.z_dim, self.channels, self.img_size).to(self.device)
        
        # Use the correct path for the model file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(current_dir, '..', 'outputs', 'models', 'generator_final.pt')
        print("Attempting to load model from:", model_path)
        
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")
        
        self.model.load_state_dict(torch.load(model_path, map_location=self.device, weights_only=True))
        self.model.eval()  # Set the model to evaluation mode

    def handle(self, data, context):
        # Generate random noise (latent vector)
        z = torch.randn(1, self.z_dim).to(self.device)
        
        # Generate the image from the noise
        with torch.no_grad():
            generated_image = self.model(z)
        
        # Convert the generated image to a PIL Image
        to_pil = transforms.ToPILImage()
        pil_image = to_pil(generated_image.squeeze(0).cpu())
        
        # Convert PIL Image to bytes
        img_byte_arr = io.BytesIO()
        pil_image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        
        return img_byte_arr