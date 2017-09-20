from flask import Flask, render_template, request, redirect, url_for
import requests
import config

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/indexData')
def get_index_data():
    breitbart = requests.get("http://beta.newsapi.org/v2/everything?source=breitbart-news&apiKey="+config.news_api['key'])
    cnn = requests.get("http://beta.newsapi.org/v2/everything?source=cnn&apiKey="+config.news_api['key'])
    fox = requests.get("http://beta.newsapi.org/v2/everything?source=fox-news&apiKey="+config.news_api['key'])