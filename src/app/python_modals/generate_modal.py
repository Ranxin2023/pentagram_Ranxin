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

