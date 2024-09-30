# src/gan_train.py

import torch
import torch.optim as optim
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from gan_models import Generator, Discriminator
import os
import matplotlib.pyplot as plt

# Hyperparameters
z_dim = 100
lr = 0.0002
batch_size = 64
epochs = 100
save_interval = 10  # Save model and images every 10 epochs

# Check if GPU is available and use it
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Define augmentations
transform = transforms.Compose([
    transforms.Resize((28, 28)),  # Resize to the target size
    transforms.Grayscale(),  # Convert to grayscale
    transforms.RandomHorizontalFlip(),  # Randomly flip images horizontally
    transforms.RandomRotation(10),  # Randomly rotate images by up to 10 degrees
    transforms.RandomResizedCrop(size=28, scale=(0.8, 1.0)),  # Crop and resize
    transforms.ColorJitter(brightness=0.2, contrast=0.2),  # Adjust brightness and contrast
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])  # Normalize to [-1, 1]
])

# Load the dataset
dataset_path = 'backend/data/images'
dataset = datasets.ImageFolder(root=dataset_path, transform=transform)

# Check if dataset is loaded
if len(dataset) == 0:
    raise ValueError("No images found in dataset folder. Please check the path.")

dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Initialize Generator and Discriminator and move them to the device (GPU or CPU)
generator = Generator(z_dim).to(device)
discriminator = Discriminator().to(device)

# Optimizers for Generator and Discriminator
optim_g = optim.Adam(generator.parameters(), lr=lr)
optim_d = optim.Adam(discriminator.parameters(), lr=lr)

# Loss function (Binary Cross Entropy Loss)
criterion = nn.BCELoss()

# Function to generate random noise (latent vector)
def generate_noise(batch_size, z_dim):
    return torch.randn(batch_size, z_dim).to(device)

# Get the absolute path of the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create absolute paths for the outputs directories
output_image_dir = os.path.join(script_dir, '../outputs/generated_images')
output_model_dir = os.path.join(script_dir, '../outputs/models')
os.makedirs(output_image_dir, exist_ok=True) # Create the directories if they don't exist
os.makedirs(output_model_dir, exist_ok=True)

# Training Loop
for epoch in range(epochs):
    for i, (real_images, _) in enumerate(dataloader):
        real_images = real_images.to(device)  # Move images to the device
        batch_size = real_images.size(0)  # Get actual batch size
        
        # Labels for real and fake data, ensuring they match the batch size and shape
        real_labels = torch.ones(batch_size, 1).to(device)  # Real images labels
        fake_labels = torch.zeros(batch_size, 1).to(device)  # Fake images labels

        # 1. Train Discriminator
        optim_d.zero_grad()
        
        # Train on real images
        outputs_real = discriminator(real_images).view(-1, 1)
        d_loss_real = criterion(outputs_real, real_labels)
        
        # Train on fake images
        z = generate_noise(batch_size, z_dim)
        fake_images = generator(z)
        outputs_fake = discriminator(fake_images.detach()).view(-1, 1)
        d_loss_fake = criterion(outputs_fake, fake_labels)

        # Total Discriminator loss
        d_loss = d_loss_real + d_loss_fake
        d_loss.backward()
        optim_d.step()

        # 2. Train Generator
        optim_g.zero_grad()
        
        # Generator wants to fool the discriminator (real_labels for fake images)
        z = generate_noise(batch_size, z_dim)
        fake_images = generator(z)
        outputs = discriminator(fake_images).view(-1, 1)
        g_loss = criterion(outputs, real_labels)

        g_loss.backward()
        optim_g.step()

    # Output loss values after each epoch
    print(f"Epoch [{epoch+1}/{epochs}], d_loss: {d_loss.item()}, g_loss: {g_loss.item()}")

    # Save generated images and model every 'save_interval' epochs
    if epoch % save_interval == 0:
        # Save generated image
        fake_img = fake_images[0].detach().cpu().numpy().reshape(28, 28)
        save_image_path = f'{output_image_dir}/epoch_{epoch}.png'
        plt.imsave(save_image_path, fake_img, cmap='gray')
        print(f"Generated image saved to {save_image_path}")
        
        # Save model
        model_save_path = f'{output_model_dir}/generator_epoch_{epoch}.pt'
        torch.save(generator.state_dict(), model_save_path)
        print(f"Generator model saved to {model_save_path}")

# Save final model after training is complete
torch.save(generator.state_dict(), f'{output_model_dir}/generator_final.pt')
torch.save(discriminator.state_dict(), f'{output_model_dir}/discriminator_final.pt')
print("Final models saved.")
