# src/gan_models.py

import torch
import torch.nn as nn

# Define the Generator model
class Generator(nn.Module):
    def __init__(self, z_dim=100):
        super(Generator, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(z_dim, 256),
            nn.ReLU(True),
            nn.Linear(256, 512),
            nn.ReLU(True),
            nn.Linear(512, 1024),
            nn.ReLU(True),
            nn.Linear(1024, 28*28),  # Output size for 28x28 images (e.g., MNIST)
            nn.Tanh()  # Tanh ensures output values are in the range [-1, 1]
        )

    def forward(self, z):
        # Reshape the output to match the 28x28 image dimensions
        return self.fc(z).view(-1, 1, 28, 28)

# Define the Discriminator model (not needed for inference, but kept here for training)
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(28 * 28, 512),  # Input is flattened 28x28 image (784 pixels)
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(256, 1),
            nn.Sigmoid()  # Sigmoid to produce a probability (real/fake)
        )

    def forward(self, x):
        # Flatten the input image (batch_size, 1, 28, 28) -> (batch_size, 28*28)
        x = x.view(x.size(0), -1)
        return self.fc(x)
