---
title: "\U0001F3B5 Video to Audio Extractor (Python)"

---

# 🎵 Video to Audio Extractor (Python)

This project allows you to extract audio from video files using **two different approaches**:

1. **FFmpeg (fast, professional, batch processing)**
2. **MoviePy (Python-only, simple, single file)**

You can choose whichever suits your workflow.

---

## 📁 Project Structure

project-folder/
│
├── videos/ # Put all your video files here
├── audios/ # Extracted audio will be saved here
│
├── Audio_extractor.py # FFmpeg based batch extractor
├── Extract.py # MoviePy based single file extractor
└── README.md

yaml
Copy code

---

## 🛠 Requirements

- Python 3.8+
- FFmpeg (for Audio_extractor.py)
- MoviePy (for Extract.py)

---

## 🔹 Method 1 — FFmpeg (Recommended)

This method is **faster, higher quality, and supports batch processing**.

### 📥 Install FFmpeg

#### Windows
1. Download FFmpeg from  
https://github.com/BtbN/FFmpeg-Builds/releases
2. Extract it (for example: `C:\ffmpeg`)
3. Add `C:\ffmpeg\bin` to **System PATH**
4. Restart Command Prompt
5. Test installation:
```bash
ffmpeg -version

▶ How to Run (FFmpeg Version)
Create folders:
videos
audios
Put all your video files inside the videos folder.

Run:
python Audio_extractor.py

🧠 What it does
For each file inside videos/, it creates:
audios/<tutorialNumber>_<videoName>.wav

Example:
videos/01.intro.mp4
→ audios/01_intro.wav

🔹 Method 2 — MoviePy (Simple, Python-Only)
This method is easy to use but slower and best for single video extraction.

📥 Install MoviePy
pip install moviepy

▶ How to Run (MoviePy Version)
Place your video in the project folder

Rename it to:
video.mp4

Run:
python Extract.py

It will generate:
audio.wav

🎚️ Audio Quality Comparison
Feature	                             FFmpeg         MoviePy
Speed	                            ⭐⭐⭐⭐⭐   ⭐⭐
Quality	                            ⭐⭐⭐⭐⭐   ⭐⭐⭐
Batch files	                         Yes	        No
Professional formats	             Yes	        Limited
Control over bitrate & sample rate   Yes	        Limited

Recommendation:
Use the FFmpeg version for AI, transcription, datasets, and professional audio extraction.

🔊 Output Format
This project outputs WAV files, which are:
Uncompressed
High-quality
Perfect for speech recognition, ML models, and editing

🚀 Use Cases
Speech-to-Text datasets
AI / ML audio training
Podcast extraction
Video lecture processing
RAG pipelines

📜 License
Free to use and modify for personal and educational purposes.
