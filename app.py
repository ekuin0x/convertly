from flask import Flask, render_template, url_for, request
import yt_dlp 
import random
from pydub import AudioSegment

import os

app = Flask(__name__)

@app.route("/") 
def index():
    return render_template("index.html")

@app.route("/getStreams/")
def getStreams():
    global url, title
    url = request.args.get("url")
    with yt_dlp.YoutubeDL() as ydl:
        meta = ydl.extract_info(url, download=False)
        formats = meta.get('formats')
        title = meta.get('title', meta)
        thumbnail = meta.get('thumbnail', meta)
        duration = int(meta.get('duration')) / 60 # minutes
   
    if duration > 45 :
        return "Error"

    else :
        res = []
        allres = ['144p', '240p', '360p', '480p', '720p', '1080p'] 

        for f in formats :
            if f['ext'] == 'mp4' :
                if 'format_note' in f :
                    if f['format_note'] in allres :  
                        res.append(f['format_note'])

        return render_template("streams.html", title = title, thumbnail = thumbnail, res = set(res))


@app.route("/getDownload/<media>/<res>")
def getDownload(media, res):
    fname = random.randint(0, 999999)
    link = f"./static/temp/{fname}"
    if media == "video" :
        resolution = res.replace('p', '')
        opts = {
            'format' : f'bestvideo[height={resolution}]+bestaudio[ext=m4a]/bestvideo[width={resolution}]+bestaudio[ext=m4a]',
            'merge_output_format' : 'mp4',
            'outtmpl' : link
        }
        with yt_dlp.YoutubeDL(opts) as ydl :
            ydl.download(url)
        return f"{fname}.mp4"
        
    elif media == "audio" : 
        opts = {
            'format' : 'bestaudio[ext=m4a]',
            'outtmpl' : link
        }
        with yt_dlp.YoutubeDL(opts) as ydl :
            ydl.download(url)

        m4aFile = AudioSegment.from_file(f"{link}.m4a", format="m4a")
        m4aFile.export(f"{link}.mp3", format='mp3')
        os.remove(f"{link}.m4a")

        return f"{fname}.mp3"
    else : 
        return "error downloading your file" 
        quit()       
        
if __name__ == "__main__" :
    app.run(debug = False)
