import youtube_dl
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("link_input.html")

@app.route("/viewer")
def viewer():
    return render_template("viewer.html")

@app.route("/linksubmit", methods=["POST", "GET"])
def submit():
    link = request.form["link"]

    ydl = youtube_dl.YoutubeDL()
    with ydl:
        result = ydl.extract_info(link, download=False)
    video = video = result["entries"][0] if "entries" in result else result
    og_link = video["webpage_url"]

    params = {"url": og_link}
    r = requests.get("https://www.tiktok.com/oembed", params=params)
    with open("templates/embed.html", "w") as f:
        f.write(r.json()["html"])

    with open("latest.txt", "w") as f:
        f.write(link)

    return """
<!DOCTYPE html>
<html>
<head>
<script>
window.location.replace("/");
</script>
</head>
</html>
"""

@app.route("/latest")
def latest():
    with open("latest.txt", "r") as f:
        return f.read()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
