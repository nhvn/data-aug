# backend/src/image_handler.py
import os
import io
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from .gan_handler import GANHandler

class ImageHandler:
    def __init__(self, use_api=True):
        self.use_api = use_api
        # Initialize GAN handler first as fallback
        print("Initializing GAN handler first")
        self.gan_handler = GANHandler()
        self.gan_handler.initialize(None)

        print(f"Initializing ImageHandler with use_api={use_api}")
        if use_api:
            try:
                api_key = os.getenv('STABILITY_API_KEY')
                print(f"API Key found: {'Yes' if api_key else 'No'}")
                
                if not api_key:
                    print("No API key found, will use GAN")
                    self.use_api = False
                else:
                    try:
                        print("Attempting to initialize Stability API...")
                        self.stability_api = client.StabilityInference(
                            key=api_key,
                            verbose=True,
                            engine='stable-diffusion-xl-1024-v1-0',
                        )
                        print("API client initialized successfully")
                        
                        # Test API with a simple request
                        print("Testing API with a simple request...")
                        test_answers = self.stability_api.generate(
                            prompt="test",
                            width=512,
                            height=512,
                            steps=1,
                            samples=1
                        )
                        next(test_answers)  # Try to get first response
                        print("API test successful")
                        
                    except Exception as e:
                        print(f"Failed to initialize or test API client: {e}, will use GAN")
                        self.use_api = False
            except Exception as e:
                print(f"Error in API setup: {e}, will use GAN")
                self.use_api = False

    def generate_image(self, input_image):  # or generate_from_image, whichever name you're using
        print(f"Original image size: {input_image.size}")
        print(f"Current API status: {self.use_api}")  # Add this debug line
        if self.use_api:
            print("Using Stability AI API for generation")
            try:
                result = self._generate_with_api(input_image)
                # Check generated image size
                if isinstance(result, bytes):
                    temp_img = Image.open(io.BytesIO(result))
                    print(f"Generated image size: {temp_img.size}")
                return result
            except Exception as e:
                print(f"API failed with error: {e}")
                print("Falling back to GAN")
                return self._generate_with_gan(input_image)
        else:
            print("Using GAN because use_api is False")  # Add this debug line
            result = self._generate_with_gan(input_image)
            return result

    MAX_DAILY_GENERATIONS = 50  # Add this at the top of your file as a global variable
    CURRENT_GENERATIONS = 0     # Add this too
    
    def _generate_with_api(self, input_image):
        try:
            print("Starting API generation")
            # Print API key status (don't print the actual key)
            print(f"API key available: {'Yes' if self.stability_api else 'No'}")
            
            # Maintain original image size but ensure it's not too large
            width, height = input_image.size
            max_size = 1024
            if width > max_size or height > max_size:
                ratio = max_size / max(width, height)
                width = int(width * ratio)
                height = int(height * ratio)
                input_image = input_image.resize((width, height), Image.Resampling.LANCZOS)
            
            # Convert PIL Image to bytes
            img_byte_arr = io.BytesIO()
            input_image.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
    
            print(f"Making API request with size: {width}x{height}")
            try:
                answers = self.stability_api.generate(
                    prompt="Create a subtle variation of this image while maintaining its overall composition",
                    init_image=input_image,
                    start_schedule=0.6,
                    seed=123,
                    steps=30,
                    cfg_scale=7.0,
                    width=width,
                    height=height,
                    samples=1,
                    sampler=generation.SAMPLER_K_DPMPP_2M
                )
                print("API request made successfully")
            except Exception as e:
                print(f"Error during API generate call: {str(e)}")
                raise
    
            for resp in answers:
                for artifact in resp.artifacts:
                    if artifact.type == generation.ARTIFACT_IMAGE:
                        print("Successfully generated image via API")
                        return artifact.binary
            
            raise ValueError("No image generated by API")
        except Exception as e:
            print(f"API generation error: {str(e)}")
            print(f"Error type: {type(e).__name__}")
            raise

    def _generate_with_gan(self, input_image):
        print("Starting GAN generation")
        try:
            result = self.gan_handler.generate_from_image(input_image)
            print("GAN generation successful")
            return result
        except Exception as e:
            print(f"GAN generation error: {e}")
            raise