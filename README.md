# Pentagram: Instagram, but with AI Images
## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [Learn More](#learn-more)
- [Usage](#usage)
- [Project Structure](#Project-structure)
- [Environment Variables](#environment-variables)
- [API Routes](#api-routes)
- [Acknowledgements](#acknowledgements)

## Introduction
Pentagram Image Generator is an AI-powered web application that transforms your imagination into stunning visuals. By leveraging the powerful Stable Diffusion model, users can input text descriptions to generate highly realistic images in just seconds. This project integrates cutting-edge technologies like Next.js for the frontend, a Modal-based backend for running the AI model, and seamless local image storage to deliver a smooth and user-friendly experience.

Whether you're an artist seeking inspiration, a developer exploring the capabilities of AI, or simply someone curious about the power of text-to-image generation, this project is built to spark creativity and showcase the future of artificial intelligence.

## Features
- Accepts text prompts and generates images using AI.
- Stores generated images locally in the file system.
- Displays the generated images on the webpage.
- Handles user input validation and error management.

## Tech Stack
- **Frontend:** React, Next.js, Tailwind CSS
- **Backend:** Node.js, Express
- **AI Model:** Stable Diffusion (via Modal)
- **Dependencies:** FastAPI, PyTorch, Diffusers, @vercel/blob

## Setup
1. Clone the GitHub repository:

```bash
git clone https://github.com/team-headstart/pentagram.git
```

2. navigate to the project directory:

```bash
cd pentagram
```

3. install the dependencies:

```bash
npm install
```
4. Run the Modal Code to Generate Modals
To enable image generation using the Stable Diffusion model, Modal is used to deploy the backend. Follow these steps:
- Navigate to the Python modal directory where the Modal scripts are located:
```sh
cd src/app/api/python_modals

```
- Deploy the Modal application by running the following command:
```sh

modal deploy generate_modal.py
```

5. Register the api key in modal:
To secure the connection between the frontend and backend, you need to register an API key in Modal:
- Log in to the Modal dashboard using your registered account: Go to [Modal Dashboard](https://modal.com/login)
- Navigate to the `Secrets` section of your deployed Modal application.
- Create a new secret by following these steps:
    - Click Create Secret.
    - Provide a name, such as IMAGE_API_KEY.
    - Add your generated API key or token (specific to your application or environment) as the value.
    - Save the secret.
- Update your project to use the secret:

    - Add the secret to the modal.Secret.from_name line in your generate_modal.py file. For example:
    ```sh
    @app.cls(image=image, gpu="T4", secrets=[modal.Secret.from_name("IMAGE_API_KEY")])
    ```
6. Run the development server:

```sh
npm run dev
```
7. Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Tasks

- Take a look at the TODOs in the repo, namely:

    - `src/app/page.tsx`: This is where the user can input their prompt and generate an image. Make sure to update the UI and handle the API response to display the images generated

    - `src/app/api/generate-image/route.ts`: This is where the image generation API is implemented. Make sure to call your image generation API from Modal here


## Learn More

To learn more about the concepts, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.
- [Modal Docuentation](https://modal.com/docs/examples/hello_world) - learn about modals
- [Nvidia GPUs](https://www.digitalocean.com/community/tutorials/h100_vs_other_gpus_choosing_the_right_gpu_for_your_machine_learning_workload) -learn more about GPUs

## Usage
- Visit http://localhost:3000 in your browser.
- Enter a text prompt describing the desired image.
- Click "Generate" to generate an image.
- View the generated image displayed on the webpage.

## Project Structure
```sh
├── public/
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   ├── generate-image/
│   │   │   │   ├── route.ts
│   │   │   │   ├── generate_image.ts
│   │   │   │   ├── python_modals/
│   │   │   │   │   ├── generate_modal.py
│   ├── pages/
│   │   ├── index.tsx
├── .env
├── package.json
├── README.md

```