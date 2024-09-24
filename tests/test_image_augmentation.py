import unittest
from torchvision import transforms
from PIL import Image
import os

class TestImageAugmentation(unittest.TestCase):

    def setUp(self):
        # Corrected to combine the directory and image file name properly
        self.image_path = os.path.join("data", "sample.jpg")  # Full path to your image
        self.image = Image.open(self.image_path)
        self.transform = transforms.RandomHorizontalFlip(p=1.0)  # Always flip for testing

    def test_horizontal_flip(self):
        # Apply the transformation
        flipped_image = self.transform(self.image)
        # Check that the image size is the same (you could extend this for more detailed checks)
        self.assertEqual(self.image.size, flipped_image.size)

if __name__ == '__main__':
    unittest.main()
