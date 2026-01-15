from moviepy.editor import VideoFileClip

# Load your video file
video = VideoFileClip("video.mp4")

# Extract audio
audio = video.audio

# Write audio to a file
audio.write_audiofile("audio.wav")
