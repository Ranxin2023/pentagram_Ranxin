"use client";

import { useState } from "react";
// import { generateImage } from "./api/generate-image/generate_image";
require('dotenv').config();

export default function Home() {
  const [inputText, setInputText] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [imageURL, setImageURL]=useState("")
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);

    try {
      // const result=await generateImage(inputText)
      const image_api_url=process.env.IMAGE_API_URL || "http://localhost:3000/api/generate-image"
      const response = await fetch(image_api_url!, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: inputText }),
      });

      const data = await response.json();
      console.log("data is: ", data);
      if(!data.success){
        throw new Error("fail to fetch the image")
      }
      // console.log("Image URL:", data.imageURL); // Debugging step
      const dataImgURL=data.imageURL as string
      // console.log("Image URL:", dataImgURL); // Debugging step
      // console.log("type of data imageurl", typeof(dataImgURL))
      setImageURL(dataImgURL); // Update state with the returned URL
      // console.log("Image URL:", dataImgURL); // Debugging step
      // if(data.imageURL){
      // }
      setInputText("");
    } catch (error) {
      console.error("Error:", error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    // TODO: Update the UI here to show the images generated
    
    <div className="min-h-screen flex flex-col justify-between p-8">
      <main className="flex-1">
        {/* Main content can go here */}
        
        {/* Display the generated image */}
        {imageURL && (
          <div className="w-full max-w-2xl rounded-lg overflow-hidden shadow-lg">
            <img
              src={imageURL}
              alt="Generated artwork"
              className="w-full h-auto"
            />
          </div>
        )}
        </main>

      <footer className="w-full max-w-3xl mx-auto">
        <form onSubmit={handleSubmit} className="w-full">
          <div className="flex gap-2">
            <input
              type="text"
              value={inputText}
              onChange={e => setInputText(e.target.value)}
              className="flex-1 p-3 rounded-lg bg-black/[.05] dark:bg-white/[.06] border border-black/[.08] dark:border-white/[.145] focus:outline-none focus:ring-2 focus:ring-black dark:focus:ring-white"
              placeholder="Describe the image you want to generate..."
              disabled={isLoading}
            />
            <button
              type="submit"
              disabled={isLoading}
              className="px-6 py-3 rounded-lg bg-foreground text-background hover:bg-[#383838] dark:hover:bg-[#ccc] transition-colors disabled:opacity-50"
            >
              {isLoading ? "Generating..." : "Generate"}
            </button>
          </div>
        </form>
      </footer>
    </div>
  );
}
