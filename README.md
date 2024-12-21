# Pentagram: Instagram, but with AI Images
## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [Usage](#usage)
- [File Structure](#file-structure)
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

## Tech Used
- **Frontend:** React, Next.js, Tailwind CSS
- **Backend:** Node.js, Express
- **AI Model:** Stable Diffusion (via Modal)
- **Dependencies:** FastAPI, PyTorch, Diffusers, @vercel/blob

## Getting Started

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
4. Register for Modal
5. Run the modal code to generate modals
6. Run the development server:

```bash
npm run dev
```

6. Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Tasks

- Take a look at the TODOs in the repo, namely:

    - `src/app/page.tsx`: This is where the user can input their prompt and generate an image. Make sure to update the UI and handle the API response to display the images generated

    - `src/app/api/generate-image/route.ts`: This is where the image generation API is implemented. Make sure to call your image generation API from Modal here


## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

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