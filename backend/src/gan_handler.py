import os
import torch
from .gan_models import Generator
from torchvision import transforms
from PIL import Image
import io
import torch.nn as nn

class Encoder(nn.Module):
    def __init__(self, img_size=64, channels=3, z_dim=100):
        super(Encoder, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(channels, 64, kernel_size=4, stride=2, padding=1),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(64, 128, kernel_size=4, stride=2, padding=1),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv2d(128, 256, kernel_size=4, stride=2, padding=1),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Flatten(),
            nn.Linear(256 * (img_size // 8) * (img_size // 8), z_dim)
        )

    def forward(self, img):
        return self.model(img)

class GANHandler:
    def __init__(self):
        self.z_dim = 100  # Latent space dimension
        self.img_size = 64  # Image size for both generator and input image
        self.channels = 3  # RGB channels

    def initialize(self, context):
        # Set the device (use GPU if available)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # Initialize the Generator and Encoder models and load weights
        self.generator = Generator(self.z_dim, self.channels, self.img_size).to(self.device)
        self.encoder = Encoder(self.img_size, self.channels, self.z_dim).to(self.device)

        # Get the current directory of the script and navigate two levels up to the root of the project
        current_dir = os.path.dirname(__file__)
        root_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))  # Go two levels up from src

        # Construct the model path relative to the root directory
        model_path = os.path.join(root_dir, 'backend', 'outputs', 'models', 'generator_final.pt')

        print("Attempting to load model from:", model_path)
        
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")
        
        self.generator.load_state_dict(torch.load(model_path, map_location=self.device))
        self.generator.eval()  # Set the generator to evaluation mode

    def generate_from_image(self, image):
        # Extract feature vector from input image
        image_tensor = self.preprocess_image(image).unsqueeze(0).to(self.device)
        feature_vector = self.encoder(image_tensor)

        # Generate new image using the feature vector
        with torch.no_grad():
            generated_image = self.generator(feature_vector)

        # Postprocess and return the generated image in byte format
        return self.postprocess_image(generated_image)

    def preprocess_image(self, image):
        transform = transforms.Compose([
            transforms.Resize((self.img_size, self.img_size)),  # Resize to match generator input
            transforms.ToTensor(),
            transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])  # Normalize between [-1, 1]
        ])
        return transform(image)

    def postprocess_image(self, image_tensor):
        # Remove batch dimension and move the tensor to CPU
        image_tensor = image_tensor.squeeze(0).cpu().detach()

        # Unnormalize the image tensor (from [-1, 1] to [0, 1])
        unnormalize = transforms.Normalize([-1, -1, -1], [2, 2, 2])
        image_tensor = unnormalize(image_tensor)

        # Convert tensor to PIL image
        pil_image = transforms.ToPILImage()(image_tensor)

        # Convert the PIL image to bytes
        img_byte_arr = io.BytesIO()
        pil_image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()  # This makes it a bytes-like object

        return img_byte_arr

