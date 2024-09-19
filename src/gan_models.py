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
            nn.Linear(1024, 28*28),  # Adjust for your dataset size (e.g., 28x28 for MNIST)
            nn.Tanh()
        )

    def forward(self, z):
        return self.fc(z).view(-1, 1, 28, 28)  # Output size should match dataset image size (e.g., 28x28)


# Define the Discriminator model
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(28 * 28, 512),  # Input size must be 28*28 = 784
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        x = x.view(x.size(0), -1)  # Flatten input image to (batch_size, 28*28)
        return self.fc(x)
