from flask import Flask, redirect, render_template, request, session, url_for
import json, os, re, requests

if os.path.exists('env.py'):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
messages = []

@app.route('/', methods = ["GET"])
def index():

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)