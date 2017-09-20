from flask import Flask, render_template, request, redirect, url_for
import requests
import config

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')
