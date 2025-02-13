import os
from pytube import YouTube
from pydub import AudioSegment

def download_youtube_audio(url, output_path):
    try:
        # Download the video
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        downloaded_file = video.download(output_path=output_path)

        # Convert to MP3
        base, ext = os.path.splitext(downloaded_file)
        mp3_file = base + '.mp3'
        
        audio = AudioSegment.from_file(downloaded_file)
        audio.export(mp3_file, format="mp3")
        
        # Optionally, remove the original downloaded file
        os.remove(downloaded_file)
        
        print(f"Downloaded and converted to MP3: {mp3_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python script.py <youtube_url> <output_path>")
        sys.exit(1)
    
    youtube_url = sys.argv[1]
    output_path = sys.argv[2]
    download_youtube_audio(youtube_url, output_path)