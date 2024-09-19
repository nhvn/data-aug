import torchvision.transforms as transforms
from PIL import Image
import torch

# Define your augmentations
data_transforms = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),  # Random horizontal flip
    transforms.RandomRotation(degrees=15),   # Random rotation up to 15 degrees
    transforms.RandomResizedCrop(size=224),  # Random crop and resize
    transforms.ColorJitter(brightness=0.2, contrast=0.2),  # Change brightness/contrast
    transforms.ToTensor()   # Convert image to tensor
])

# Load an image and apply augmentations
img = Image.open('../data/sample.jpg')  # Replace with your image path
augmented_img_tensor = data_transforms(img)  # Apply transformations

# Convert the tensor back to a PIL image
to_pil = transforms.ToPILImage()
augmented_img = to_pil(augmented_img_tensor)

# Save the augmented image
augmented_img.save('../data/augmented_image.jpg')  # Save to the 'data' folder
