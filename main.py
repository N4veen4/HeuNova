from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
import uvicorn
import os
import cv2
import numpy as np
import base64
from io import BytesIO
from PIL import Image

from colorizer import ImageColorizer
from utils import preprocess_image, postprocess_image

app = FastAPI(title="HueNova AI - Image Colorization")

# Initialize Colorizer
try:
    colorizer = ImageColorizer(model_dir="models")
except Exception as e:
    print(f"Error loading model: {e}")
    colorizer = None

# Ensure static directory exists
os.makedirs("static", exist_ok=True)

@app.post("/api/colorize")
async def colorize_image(file: UploadFile = File(...)):
    if not colorizer:
        return JSONResponse(content={"error": "Model not loaded"}, status_code=500)
    
    try:
        content = await file.read()
        # Preprocess
        original_img, l_channel, _ = preprocess_image(content)
        
        # Colorize
        ab_predicted = colorizer.colorize(l_channel)
        
        # Postprocess
        result_bgr = postprocess_image(l_channel, ab_predicted, original_img.shape)
        
        # Convert to RGB for display
        result_rgb = cv2.cvtColor(result_bgr, cv2.COLOR_BGR2RGB)
        
        # Encode to base64
        _, buffer = cv2.imencode('.png', result_bgr) # Save as BGR for imencode (which expects BGR for .png)
        img_base64 = base64.b64encode(buffer).decode('utf-8')
        
        return {
            "result": f"data:image/png;base64,{img_base64}"
        }
        
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    print("🚀 Starting HueNova AI Server...")
    print("📦 Loading AI model... please wait.")
    print("\n✅ Server Ready!")
    print("🔗 Click here to open the project: http://127.0.0.1:8000")
    print("-" * 50)
    uvicorn.run(app, host="127.0.0.1", port=8000)
