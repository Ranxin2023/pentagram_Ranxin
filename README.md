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


## Features
- Accepts text prompts and generates images using AI.
- Stores generated images locally in the file system.
- Displays the generated images on the webpage.
- Handles user input validation and error management.


## Getting Started

First, clone the GitHub repository:

```bash
git clone https://github.com/team-headstart/pentagram.git
```

Then, navigate to the project directory:

```bash
cd pentagram
```

Then, install the dependencies:

```bash
npm install
```

Run the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

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
│   │   │   │   ├── utils/
│   │   │   │   │   ├── generate_modal.py
│   ├── pages/
│   │   ├── index.tsx
├── .env
├── package.json
├── README.md

```