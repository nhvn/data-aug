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

# Check if GPU is available and use it
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Define augmentations
transform = transforms.Compose([
    transforms.Resize((28, 28)),  # Resize to the target size
    transforms.Grayscale(),  # Convert to grayscale if needed
    transforms.RandomHorizontalFlip(),  # Randomly flip images horizontally
    transforms.RandomRotation(10),  # Randomly rotate images by up to 10 degrees
    transforms.RandomResizedCrop(size=28, scale=(0.8, 1.0)),  # Crop and resize
    transforms.ColorJitter(brightness=0.2, contrast=0.2),  # Adjust brightness and contrast
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])  # Normalize to [-1, 1]
])

dataset_path = '../data/your_dataset_folder'
dataset = datasets.ImageFolder(root='../data/your_dataset_folder', transform=transform)

# Check if dataset is loaded
if len(dataset) == 0:
    print("No images found in dataset folder. Please check the path.")
    exit()

dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Create Generator and Discriminator and move them to the device (GPU or CPU)
generator = Generator(z_dim).to(device)
discriminator = Discriminator().to(device)

# Optimizers
optim_g = optim.Adam(generator.parameters(), lr=lr)
optim_d = optim.Adam(discriminator.parameters(), lr=lr)

# Loss function
criterion = nn.BCELoss()

# Function to generate random noise
def generate_noise(batch_size, z_dim):
    return torch.randn(batch_size, z_dim).to(device)

# Create output directory for generated images if it doesn't exist
output_dir = '../outputs/generated_images'
os.makedirs(output_dir, exist_ok=True)

# Training Loop
for epoch in range(epochs):
    for i, (real_images, _) in enumerate(dataloader):
        real_images = real_images.to(device)  # Move images to the device
        batch_size = real_images.size(0)  # Get actual batch size
        
        # Print batch size for debugging
        print(f"Batch size: {batch_size}")

        # Labels for real and fake data, ensuring they match the batch size and shape
        real_labels = torch.ones(batch_size).to(device)  # 1D tensor
        fake_labels = torch.zeros(batch_size).to(device)  # 1D tensor

        # Train Discriminator
        optim_d.zero_grad()
        outputs = discriminator(real_images).view(-1)  # Flatten the Discriminator output to match labels
        
        # Print output and label sizes for debugging
        print(f"Discriminator output size: {outputs.size()}, Real label size: {real_labels.size()}")
        
        d_loss_real = criterion(outputs, real_labels)  # Use flattened labels

        # Generate fake images
        z = generate_noise(batch_size, z_dim)  # Ensure noise matches batch_size
        fake_images = generator(z)
        outputs = discriminator(fake_images.detach()).view(-1)  # Flatten the output
        
        # Print output and label sizes for debugging
        print(f"Discriminator fake output size: {outputs.size()}, Fake label size: {fake_labels.size()}")

        d_loss_fake = criterion(outputs, fake_labels)  # Use flattened labels

        # Backpropagation and optimization for Discriminator
        d_loss = d_loss_real + d_loss_fake
        d_loss.backward()
        optim_d.step()

        # Train Generator
        optim_g.zero_grad()
        z = generate_noise(batch_size, z_dim)
        fake_images = generator(z)
        outputs = discriminator(fake_images).view(-1)  # Flatten the output
        g_loss = criterion(outputs, real_labels)  # Use flattened labels

        # Backpropagation and optimization for Generator
        g_loss.backward()
        optim_g.step()

    # Output loss values
    print(f"Epoch [{epoch+1}/{epochs}], d_loss: {d_loss.item()}, g_loss: {g_loss.item()}")

    # Save generated images every 10 epochs
    if epoch % 10 == 0:
        fake_img = fake_images[0].detach().cpu().numpy().reshape(28, 28)
        save_path = f'{output_dir}/epoch_{epoch}.png'
        plt.imsave(save_path, fake_img, cmap='gray')
        print(f"Generated image saved to {save_path}")

