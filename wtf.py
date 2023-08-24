from pytube import YouTube
from pytube.cli import on_progress 

url = "https://www.youtube.com/watch?v=1W3Sfoi5oFY&ab_channel=HenryMoodie"
yt = YouTube(url,on_progress_callback=on_progress)
video = yt.streams.filter(only_audio=True).first()
video.download()



