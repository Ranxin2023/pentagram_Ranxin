import modal
import io
import torch
from diffusers import AutoPipelineForText2Image
from fastapi import FastAPI, HTTPException, Query, Request, Response
from io import BytesIO
from datetime import datetime, timezone
import os
import requests


def download_modal():
    AutoPipelineForText2Image.from_pretrained(
            "stabilityai/sdxl-turbo",
            torch_dtype=torch.float16,
            variant="fp16"
        )
# Initialize Modal app
# Define the Modal image with required dependencies
image = (modal.Image.debian_slim().pip_install("fastapi[standard]","transformers","accelerate", "diffusers","requests").run_function(download_modal))
# Define the FastAPI app
# fastapi_app = FastAPI()
# Stable Diffusion Model
app = modal.App("stable-diffusion-t4", image=image)
@app.function(image=image)
def verify_torch():
    import torch
    print("Torch version:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())
@app.function(image=image)
def verify_environment():
    # Load environment variables from .env file
    # load_dotenv()
    
    if os.environ["MODAL_API_KEY"]:
        print("load env successfully", os.environ["MODAL_API_KEY"])
@app.cls(image=image, gpu="T4", secrets=[modal.Secret.from_name("modal-ranxin")])
class Model:
    @modal.build()
    @modal.enter()
    def load_weights(self):
        print("Initializing Stable Diffusion pipeline...")
        # Load the Stable Diffusion model
        self.pipe = AutoPipelineForText2Image.from_pretrained(
            "stabilityai/sdxl-turbo",
            torch_dtype=torch.float16,
            variant="fp16"
        )
        self.pipe.to("cuda")  # Use the GPU
        self.API_KEY = os.environ.get("MODAL_API_KEY")
        print(f"API Key loaded: {self.API_KEY}")
    
    @modal.web_endpoint()
    async def health(self):
        """Health check endpoint."""
        return {"status": "healthy", "timestamp": datetime.now(timezone.utc).isoformat()}

    @modal.web_endpoint()
    def generate(self, request: Request, prompt: str = Query(..., description="Text prompt for image generation")):
        print("Generate an image from a text prompt:", prompt)
        api_key = request.headers.get("X-API-Key")
        print("Self api key is", self.API_KEY)
        if api_key != self.API_KEY:
            raise HTTPException(
                status_code=401,
                detail="Unauthorized"
            )
        image = self.pipe(prompt, num_inference_steps=1, guidance_scale=0.0).images[0]

        buffer = io.BytesIO()
        image.save(buffer, format="JPEG")
        buffer.seek(0)

        return Response(content=buffer.getvalue(), media_type="image/jpeg")


# Keep the app warm (optional)
@app.function(schedule=modal.Cron("*/5 * * * *"))
def keep_warm():
    """Ping the health endpoint every 5 minutes to keep the app warm."""
    health_url = "https://ranxinli2024--stable-diffusion-t4-model-health.modal.run"
    api_key = os.environ['MODAL_API_KEY']
    headers = {"X-API-Key": api_key}

    # Ping the health endpoint
    health_response = requests.get(health_url, headers=headers)
    print(f"Health check: {health_response.status_code} at {datetime.now(timezone.utc).isoformat()}")

# # Local entrypoint for testing or running the FastAPI app
# @app.local_entrypoint()
# def main():
#     print("Testing the generate function...")

#     # Test Prompt
#     test_prompt = "A futuristic cityscape with flying cars at sunset"

#     # Test the generate function
#     # from fastapi.testclient import TestClient

#     # Create a FastAPI Test Client
#     # client = TestClient(fastapi_app)
#     generate_url="https://ranxinli2024--stable-diffusion-t4-model-generate-dev.modal.run"
#     # Call the /generate endpoint
#     headers = {"X-API-Key": os.getenv('IMAGE_API_KEY')}  # Replace with your actual API key
#     # print("API key is", os.getenv('IMAGE_API_KEY'))
#     params = {"prompt": test_prompt}

#     response = requests.post(generate_url, params=params, headers=headers)

#     # Handle the response
#     if response.status_code == 200:
#         with open("generated_image.jpg", "wb") as f:
#             f.write(response.content)
#         print("Image generated and saved as 'generated_image.jpg'")
#     else:
#         print(f"Error: {response.status_code}, {response.json()}")

# from unittest.mock import Mock
# from fastapi import HTTPException, Query
# from io import BytesIO
# from PIL import Image

# # Create a mock Request object
# mock_request = Mock()
# mock_request.headers = {"X-API-Key": "test_api_key"}

# # Mock environment variable for the API key
# import os
# # os.environ["MODAL_API_KEY"] = "test_api_key"

# # Initialize the Model instance
# model_instance = Model()

# # Mock the pipeline
# class MockPipeline:
#     def __call__(self, prompt, num_inference_steps, guidance_scale):
#         print(f"Pipeline called with prompt: {prompt}")
#         # Create a mock image
#         img = Image.new("RGB", (512, 512), color="blue")  # A blue image
#         return Mock(images=[img])

# # Replace the actual pipeline with the mock pipeline
# model_instance.pipe = MockPipeline()
# model_instance.API_KEY = os.environ["IMAGE_API_KEY"]

# # Define the test function
# def test_generate():
#     prompt = "A beautiful sunset over a mountain lake."
#     try:
#         # Call the generate method
#         response = model_instance.generate(mock_request, prompt=prompt)
#         print("Test successful! Image generated.")

#         # Verify the response content
#         buffer = BytesIO(response.body)
#         image = Image.open(buffer)
#         image.verify()  # Ensure it's a valid image
#         print("Image verification passed.")

#         # Optionally save the image to inspect it locally
#         buffer.seek(0)
#         with open("test_output.jpg", "wb") as f:
#             f.write(buffer.getvalue())
#         print("Image saved as 'test_output.jpg'.")

#     except HTTPException as e:
#         print(f"HTTPException raised: {e.detail}")
#     except Exception as e:
#         print(f"Test failed: {e}")

# # Run the test
# test_generate()
