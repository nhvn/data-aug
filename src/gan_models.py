# src/gan_train.py

import torch
import torch.optim as optim
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from gan_models import Generator, Discriminator

# Hyperparameters
z_dim = 100
lr = 0.0002
batch_size = 64
epochs = 100

# Load Dataset (adjust size if needed)
transform = transforms.Compose([
    transforms.Resize((28, 28)),  # Adjust size if needed
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])  # Normalize images to [-1, 1]
])
dataset = datasets.ImageFolder(root='../data/your_dataset_folder', transform=transform)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Create Generator and Discriminator
generator = Generator(z_dim)
discriminator = Discriminator()

# Optimizers
optim_g = optim.Adam(generator.parameters(), lr=lr)
optim_d = optim.Adam(discriminator.parameters(), lr=lr)

# Loss function
criterion = nn.BCELoss()

# Function to generate random noise
def generate_noise(batch_size, z_dim):
    return torch.randn(batch_size, z_dim)

# Training Loop
for epoch in range(epochs):
    for real_images, _ in dataloader:
        batch_size = real_images.size(0)  # Get actual batch size

        # Labels for real and fake data
        real_labels = torch.ones(batch_size, 1)
        fake_labels = torch.zeros(batch_size, 1)

        # Train Discriminator
        optim_d.zero_grad()
        outputs = discriminator(real_images)
        d_loss_real = criterion(outputs, real_labels)

        # Generate fake images
        z = generate_noise(batch_size, z_dim)
        fake_images = generator(z)
        outputs = discriminator(fake_images.detach())
        d_loss_fake = criterion(outputs, fake_labels)

        # Backpropagation and optimization for Discriminator
        d_loss = d_loss_real + d_loss_fake
        d_loss.backward()
        optim_d.step()

        # Train Generator
        optim_g.zero_grad()
        z = generate_noise(batch_size, z_dim)
        fake_images = generator(z)
        outputs = discriminator(fake_images)
        g_loss = criterion(outputs, real_labels)

        # Backpropagation and optimization for Generator
        g_loss.backward()
        optim_g.step()

    print(f"Epoch [{epoch}/{epochs}], d_loss: {d_loss.item()}, g_loss: {g_loss.item()}")

    # Optionally, save generated images to 'outputs/'
    if epoch % 10 == 0:
        fake_img = fake_images[0].detach().cpu().numpy().reshape(28, 28)
        save_path = f'../outputs/generated_images/epoch_{epoch}.png'
        import matplotlib.pyplot as plt
        plt.imsave(save_path, fake_img, cmap='gray')
        print(f"Generated image saved to {save_path}")
