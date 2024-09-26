import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader

# Define augmentations (same as before)
data_transforms = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(degrees=15),
    transforms.RandomResizedCrop(size=224),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
    transforms.ToTensor()
])

# Load the dataset and apply augmentations
dataset = ImageFolder(root='../data/your_dataset_folder', transform=data_transforms)

# Set up DataLoader to load the data in batches
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Iterate through the DataLoader to get augmented images
for batch_idx, (images, labels) in enumerate(dataloader):
    print(f"Batch {batch_idx + 1}:")
    print(f"Images Shape: {images.shape}")  # Shape will be [batch_size, channels, height, width]
    print(f"Labels: {labels}")  # Labels will correspond to the class of each image
    # Here you can use these images in your training loop or do further processing
