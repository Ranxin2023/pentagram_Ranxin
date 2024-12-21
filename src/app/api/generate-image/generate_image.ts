"use server";
export async function generateImage(text: string) {
    try {
        // Sending a POST request to the server
        const response = await fetch('http://localhost:3000/api/generate-image', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-API-SECRET': process.env.API_SECRET || '', // API secret from the environment variable
            },
            body: JSON.stringify({ prompt: text }), // The text prompt sent to the server
        });

        // Checking for a successful response
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Extracting the response data
        const data = await response.json();
        return {
            success: true,
            data,
        };
    } catch (error) {
        console.error('Server Error:', error);

        // Return an error object
        return {
            success: false,
            error: error instanceof Error ? error.message : 'Failed to generate image',
        };
    }
}
