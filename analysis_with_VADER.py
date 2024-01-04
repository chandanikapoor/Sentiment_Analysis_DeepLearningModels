import pandas as pd
import nltk as nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def perform_sentiment_analysis(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores["compound"]

def analyze_sentiment(csv_filename='comments.csv', output_filename='sentiment_analysis.csv'):
    # Read the CSV file
    df = pd.read_csv(csv_filename)

    # Perform sentiment analysis on each comment
    df['sentiment_score'] = df['body'].apply(perform_sentiment_analysis)

    # Save the results to a new CSV file
    df.to_csv(output_filename, index=False)

if __name__ == "__main__":
    analyze_sentiment('comments.csv', 'sentiment_analysis.csv')
