# src/gan_handler.py

import torch
from gan_models import Generator

class GANHandler:
    def __init__(self):
        self.z_dim = 100  # Latent space dimension

    def initialize(self, context):
        # Set the device (use GPU if available)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # Initialize the Generator model and load weights
        self.model = Generator(self.z_dim).to(self.device)
        model_path = '../outputs/models/generator_final.pt'
        self.model.load_state_dict(torch.load(model_path, map_location=self.device))
        self.model.eval()  # Set the model to evaluation mode

    def handle(self, data, context):
        # Generate random noise (latent vector)
        batch_size = 1  # Generate 1 image per request; you can adjust this
        z = torch.randn(batch_size, self.z_dim).to(self.device)

        # Generate the image from the noise
        with torch.no_grad():
            generated_image = self.model(z).cpu().numpy()

        # Convert the generated image to a list and return
        return generated_image.tolist()
