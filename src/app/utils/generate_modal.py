import modal

# Define the app
app = modal.App("image-generation-api")

# Define an image generation function
@app.function()
def generate_image(prompt: str):
    # Replace this with your Stable Diffusion or Image Generation logic
    return f"Image generated for prompt: {prompt}"

# Expose the function as a web endpoint
@app.local_entrypoint()
def main():
    print("Deploying API...")
    app.deploy()
