import torchvision.transforms as transforms
from PIL import Image
import os

# Define your augmentations
data_transforms = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),  # Random horizontal flip
    transforms.RandomRotation(degrees=15),   # Random rotation up to 15 degrees
    transforms.RandomResizedCrop(size=224),  # Random crop and resize
    transforms.ColorJitter(brightness=0.2, contrast=0.2),  # Adjust brightness and contrast
    transforms.ToTensor()   # Convert image to tensor
])

def augment_data(dataset):
    """Applies transformations to the dataset of images."""
    augmented_data = []
    for image_path in dataset:
        img = Image.open(image_path)
        augmented_img_tensor = data_transforms(img)  # Apply transformations
        augmented_data.append(augmented_img_tensor)
    return augmented_data

def save_images(augmented_data, output_dir):
    """Saves augmented images to the specified directory."""
    to_pil = transforms.ToPILImage()
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for i, img_tensor in enumerate(augmented_data):
        img = to_pil(img_tensor)  # Convert tensor back to PIL image
        img.save(os.path.join(output_dir, f'augmented_image{i + 1}.jpg'))
