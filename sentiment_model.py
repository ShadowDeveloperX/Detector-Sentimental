import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """
    Analiza el sentimiento de un texto dado.
    Retorna una etiqueta: Positivo, Negativo o Neutral.
    """
    score = sia.polarity_scores(text)
    if score['compound'] > 0.05:
        return "Positivo"
    elif score['compound'] < -0.05:
        return "Negativo"
    else:
        return "Neutral"
