from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    yorum = ""
    try:
        with open("yorum.txt", "r", encoding="utf-8") as f:
            yorum = f.read()
    except:
        yorum = "Yorum bulunamadı."

    return render_template("index.html", yorum=yorum)

# app.run() satırı kaldırıldı, gunicorn ile çalışacak
