import os
import io
import requests
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from .gan_handler import GANHandler

class ImageHandler:
    def __init__(self, use_api=True):
        self.use_api = use_api
        if use_api:
            api_key = os.getenv('STABILITY_API_KEY')
            if not api_key:
                raise ValueError("STABILITY_API_KEY not found in environment variables")
            self.stability_api = client.StabilityInference(
                key=api_key,
                verbose=True,
            )
        else:
            self.gan_handler = GANHandler()
            self.gan_handler.initialize(None)

    def generate_image(self, input_image):
        if self.use_api:
            return self._generate_with_api(input_image)
        else:
            return self._generate_with_gan(input_image)

    def _generate_with_api(self, input_image):
        # Convert PIL Image to bytes
        img_byte_arr = io.BytesIO()
        input_image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        # Generate image using Stability API
        answers = self.stability_api.generate(
            prompt="enhance this image",
            init_image=input_image,
            start_schedule=0.6,
            seed=123,
            steps=30,
            cfg_scale=7.0,
            width=512,
            height=512,
            samples=1,
        )

        # Process and return the generated image
        for resp in answers:
            for artifact in resp.artifacts:
                if artifact.type == generation.ARTIFACT_IMAGE:
                    return artifact.binary

    def _generate_with_gan(self, input_image):
        # Your existing GAN generation code
        return self.gan_handler.generate_from_image(input_image)