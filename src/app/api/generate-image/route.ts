import { put } from "@vercel/blob";
import { NextResponse } from "next/server";
import crypto from "crypto"
import { access } from "fs";
import fs from "fs";
import path from "path";
export async function POST(request: Request) {
  try {
    const body = await request.json();
    const { text } = body;
    console.log("text get from client:", text)
    // TODO: Call your Image Generation API here
    // For now, we'll just echo back the text
    if (!text || typeof text !== "string") {
      return NextResponse.json(
        { success: false, error: "Text input is required and must be a string" },
        { status: 400 }
      );
    }
    const generateURL=process.env.GENERATE_URL
    console.log("generate URl is", generateURL)
    const url=new URL(generateURL!)
    url.searchParams.set("prompt", text)
    // Call Modal's Image Generation API
    console.log("api key is", process.env.IMAGE_API_KEY)
    const response = await fetch(url.toString(), {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "X-API-Key": `${process.env.IMAGE_API_KEY}`, // Use your token_id
        Accept:"image/jpeg"
      },
      
    });

    if (!response.ok) {
      throw new Error("Failed to fetch image from API");
    }
    // const data = await response.json();
    const imageBuffer = Buffer.from(await response.arrayBuffer());
    const filename=`${crypto.randomUUID()}.jpg`
     // Define the directory where files will be stored
     const saveDirectory = path.join(process.cwd(), "public", "images");
     const filePath = path.join(saveDirectory, filename);
 
     // Ensure the directory exists
     if (!fs.existsSync(saveDirectory)) {
       fs.mkdirSync(saveDirectory, { recursive: true });
     }
 
     // Write the image buffer to the local file system
     fs.writeFileSync(filePath, imageBuffer);
     const imageUrl = `http://localhost:3000/images/${filename}`;
     return NextResponse.json({
       success: true,
       imageURL: imageUrl, // Return the relative path for the frontend
       message: `Image successfully generated and saved: ${text}`,
     });
  } catch (error:any) {
    console.error("Error is", error)
    return NextResponse.json(
      { success: false, error: "Failed to process request" },
      { status: 500 }
    );
  }
}
