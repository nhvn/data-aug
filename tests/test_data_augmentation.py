import unittest
import sys
import os

# Add the src directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Correct import from augment_images.py
from augment_images import augment_data, save_images

class TestDataAugmentationPipeline(unittest.TestCase):

    def test_augmentation_pipeline(self):
        # Load test dataset
        dataset = self.load_test_data()  # Replace with your actual function for loading a dataset

        # Apply augmentations
        augmented_data = augment_data(dataset)

        # Save the augmented images
        output_dir = "output_dir"
        os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist
        save_images(augmented_data, output_dir)

        # Verify that at least one image is saved correctly
        self.assertTrue(os.path.exists(os.path.join(output_dir, "augmented_image1.jpg")))

    def load_test_data(self):
        # Replace this with actual dataset loading logic
        return ["data/your_dataset_folder/sample1.jpg", "data/your_dataset_folder/sample2.jpg"]

if __name__ == '__main__':
    unittest.main()
