import moviepy.editor as mp
from pytube import YouTube


yt = YouTube('https://www.youtube.com/watch?v=1W3Sfoi5oFY&ab_channel=HenryMoodie')
stream = yt.streams.filter(progressive=True).last()
streamSize = stream.filesize
print(streamSize)








