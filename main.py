from flask import Flask, render_template, url_for, request
import yt_dlp 
import random
import Cryptodome

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
    resolution = res.replace('p', '')
    print(f'bestvideo[height={resolution}][ext=mp4]+bestaudio')
    fname = random.randint(0, 99999)
    link = f"./static/temp/{fname}"
    if media == "video" :
        opts = {
            'format' : 'bestvideo[height=240]+bestaudio[ext=m4a]/bestvideo[width=240]+bestaudio[ext=m4a]',
            'merge_output_format' : 'mp4',
            'outtmpl' : link
        }
        with yt_dlp.YoutubeDL(opts) as ydl :
            ydl.download(url)
        return f"{link}.mp4"
        
    elif media == "audio" : 
        link = 'temp/'+str(random.randint(0.99999))+'.mp4'
        opts = {
            'format' : 'bestaudio[ext=mp3]/bestaudio[ext=m4a]',
            'merge_output_format' : 'mp4',
            'outtmpl' : 'static/temp/'+ str(random.randint(0,99999))
            }
        with yt_dlp.YoutubeDL(opts) as ydl :
            ydl.download(url)
        return f"{link}.mp3"
    else : 
        return "error downloading your file" 
        quit()       
        
if __name__ == "__main__" :
    app.run(debug = True)
