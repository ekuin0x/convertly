from flask import Flask, render_template, url_for, request
from pytube import YouTube
import moviepy.editor as mp

import os

app = Flask(__name__)

@app.route("/") 
def index():
    return render_template("index.html")

@app.route("/getStreams/")
def getStreams():
    url = request.args.get("url")
    global yt 
    yt = YouTube(url)
    myStreams = yt.streams.filter(progressive = True)
    return render_template("streams.html", streams = myStreams)

@app.route("/getDownload/<media>/<res>")
def getDownload(media, res):
    global stream
    stream = yt.streams.filter(progressive=True, res = res).first()

    if media == "video" :
        stream.download()
        return f"Downloading your video : <b>{stream.title}</b> " 
        
    elif media == "audio" : 
        stream.download()
        clip = mp.VideoFileClip(f"{stream.title}.mp4" )
        clip.audio.write_audiofile(f"${stream.title}.mp3")
        return "Audio Downloading"
    else : 
        return "error downloading your file" 
        quit()       
    

@app.route('/getProgress')
def getProgress():
    streamSize = stream.filesize
    mediaExtension = "mp3" if media == "audio" else "mp4"
    download = f"/{stream.title}.${mediaExtension}"
    downloaded = os.stat(file_name).st_size

    progress = (downloaded / streamSize) * 100
 
    return progress
        

    

if __name__ == "__main__" :
    app.run(debug = True)
