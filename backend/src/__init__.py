from .gan_handler import GANHandler
from .gan_models import Generator
from .image_handler import ImageHandler

__all__ = ['GANHandler', 'Generator', 'ImageHandler']

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