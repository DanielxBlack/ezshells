#!/usr/bin/env python3

from flask import render_template, request
from app import app


@app.route("/")
@app.route("/index")
def index():
    # name = request.args["attackerIP", "listeningPort", "language"]
    return render_template("index.html", name="EZShellz")
