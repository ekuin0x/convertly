from flask import Flask, render_template, url_for, request
import yt_dlp 
import random
from pydub import AudioSegment

import os

app = Flask(__name__)

@app.route("/") 
def index():
    f = open('hello.text', 'w' )
    f.write("wtf")
    return render_template("index.html")


if __name__ == "__main__" :
    app.run(debug = False)
