# TikTok Viewer

This code implements a simple Flask application enabling users to watch TikToks
together. There is a page to submit links, and a page to view links. When a
link is submitted, the embedded TikTok video on the view page automatically
updates.

This project can be used by two people to watch TikToks together remotely if
run on a server, or it can be run on a computer connected to a projector to
allow anyone to show TikTok videos on a primary screen.

# Quick Start

Install requirements by running

```
python3 -m pip install --upgrade --requirement requirements.txt
```

Then run the program by doing

```
python3 main.py
```

To submit TikTok links, connect to `http://localhost:5000`. To view the latest
synced link, connect to `http://localhost:5000/viewer`.

# Project Status

This project was a one-off application, written quickly. It will not be
maintained. It has minimal documentation.
