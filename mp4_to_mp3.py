from pydub import AudioSegment

# Load the MP4 file
mp4_file = AudioSegment.from_file("example.mp4", format="mp4")

# Export the MP4 file as MP3
mp4_file.export("example.mp3", format="mp3")
