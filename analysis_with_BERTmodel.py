import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax

def analyze_sentiment_bert(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    probabilities = softmax(logits, dim=1).detach().numpy()[0]

    # Assuming 0 corresponds to negative, 1 to neutral, and 2 to positive sentiment
    sentiment_score = probabilities[2] - probabilities[0]
    return sentiment_score

def analyze_sentiments_bert_on_comments(csv_filename='comments.csv', output_filename='sentiment_analysis_bert.csv'):
    # Load the BERT model and tokenizer
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3)

    # Read the CSV file containing comments
    df = pd.read_csv(csv_filename)

    # Perform sentiment analysis on each comment
    df['sentiment_score'] = df['body'].apply(lambda x: analyze_sentiment_bert(x, model, tokenizer))

    # Save the results to a new CSV file
    df.to_csv(output_filename, index=False)

if __name__ == "__main__":
    analyze_sentiments_bert_on_comments('comments.csv', 'sentiment_analysis_bert.csv')
    


# Load the ground truth labels and predicted labels
ground_truth = pd.read_csv('ground_truth.csv')['sentiment_label']
predicted_labels = pd.read_csv('predicted_labels.csv')['sentiment_label']

# Calculate accuracy
accuracy = accuracy_score(ground_truth, predicted_labels)
print(f"Accuracy: {accuracy}")

