from flask import Flask, render_template, request, redirect, url_for
import requests
import config

app = Flask(__name__, static_url_path='')

apiKey = "apiKey=" + config.news_api['key']
newsApiEverythingUrl = "http://beta.newsapi.org/v2/everything?"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/everthingData')
def get_index_data():
    sourcesObject = {}
    sources = ['breitbart', 'cnn', 'fox-news'] # for final release - request.args.getlist('sources')
    for source in sources:
        sourcesObject[source] = requests.get(newsApiEverythingUrl + "source=" + source + apiKey)
    return sourcesObject
