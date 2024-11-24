from fastapi import FastAPI, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import yt_dlp

# Create FastAPI app
app = FastAPI()

# Enable CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Set the current directory
cur_dir = os.getcwd()

@app.post("/download")
def download_video(link: str = Form(...)):
    youtube_dl_options = {
        "format": "best",
        "outtmpl": os.path.join(cur_dir, f"video-{link[-11:]}.mp4")
    }

    try:
        with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
            ydl.download([link])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"status": "Download started"}