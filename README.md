# **YouTube Video Downloader**

## Description
This project is a simple YouTube video downloader built using FastAPI for the backend and HTML/CSS/JavaScript for the frontend. Users can paste a YouTube video URL and select the quality of the video they wish to download.

## Features
- **Paste a YouTube URL to fetch video information.**
- **Select the desired video quality before downloading.**
- **Fast and efficient video downloading using `yt-dlp`.**
- **User-friendly interface.**

## Technologies Used
- **Backend:** FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **Video Downloading:** yt-dlp
- **Python:** v3.x

## Requirements
- **Python 3.x**
- **FastAPI**
- **yt-dlp**
- **Uvicorn** (for running the FastAPI app)

## Installation Require Packages

1. **Clone the repository:**
   ```bash
   https://github.com/Jhanesh/youtube_video_downloader.git
   cd youtube-video-downloader

2. **yt-dlp uvicorn**
   ```bash
   pip install fastapi yt-dlp uvicorn

## Usage

1. **Start the FastAPI server:**
   To run the backend server, execute the following command in your terminal:
   ```bash
   uvicorn app:app --reload
2.**Open the web application:**
  In your web browser, navigate to the index.html file located in the project directory to access the user interface.

3.**Fetch Video Information:**
  Paste the YouTube video URL into the input box provided.
  Click the "Fetch Video Info" button to retrieve the video details.

4.**Select Video Quality:**
  After fetching the video info, a dropdown menu will display the available video quality options.
  Choose your preferred quality from the dropdown list.

5.**Download the Video:**
  Click the "Download" button to initiate the download of the video in the selected quality.
  The video will start downloading to your device.

## API Endpoints
- **POST /fetch_video_info:** Accepts a JSON object containing the YouTube URL and returns available video formats and qualities.
- **GET /download_video:** Accepts the URL and selected quality to download the video.

## Troubleshooting
1. If you encounter issues fetching video information, ensure that the URL is valid and the backend is running correctly.
2. Check your browser's console for any error messages.

## License
This project is licensed under the MIT License.

## Author
- Jhanesh V
- jhaneshvanka@gmail.com
- https://github.com/Jhanesh
