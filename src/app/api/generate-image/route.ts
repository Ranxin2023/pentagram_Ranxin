import { NextResponse } from "next/server";

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { text } = body;

    // TODO: Call your Image Generation API here
    // For now, we'll just echo back the text
    if (!text || typeof text !== "string") {
      return NextResponse.json(
        { success: false, error: "Text input is required and must be a string" },
        { status: 400 }
      );
    }
    // Call Modal's Image Generation API
    const response = await fetch(process.env.IMAGE_API_URL!, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${process.env.API_KEY}`, // Use your token_id
      },
      body: JSON.stringify({
        prompt: text, // Input text for image generation
      }),
    });

    if (!response.ok) {
      throw new Error("Failed to fetch image from API");
    }

    const data = await response.json();
    return NextResponse.json({
      success: true,
      message: `Received: ${text}`,
    });
  } catch (error) {
    return NextResponse.json(
      { success: false, error: "Failed to process request" },
      { status: 500 }
    );
  }
}
