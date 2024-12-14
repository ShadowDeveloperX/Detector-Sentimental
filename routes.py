from flask import Flask, render_template, request
from model.sentiment_model import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    user_text = request.form['text']
    sentiment = analyze_sentiment(user_text)
    return render_template('result.html', text=user_text, sentiment=sentiment)
