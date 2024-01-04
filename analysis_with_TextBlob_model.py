import pandas as pd
import textblob as textblob
from textblob import TextBlob

def perform_textblob_sentiment_analysis(data):
    # Perform sentiment analysis using TextBlob
    sentiment_scores = data.apply(lambda x: TextBlob(x).sentiment.polarity)
    return sentiment_scores

def main():
    # Load comments data
    df = pd.read_csv('comments.csv')

    # Perform TextBlob sentiment analysis
    sentiment_scores = perform_textblob_sentiment_analysis(df['body'])

    # Add sentiment scores to the DataFrame
    df['sentiment_score'] = sentiment_scores

    # Save the results to a new CSV file
    df.to_csv('sentiment_analysis_textblob.csv', index=False)

if __name__ == "__main__":
    main()
