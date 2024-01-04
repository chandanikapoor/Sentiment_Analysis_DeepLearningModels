import pandas as pd

# Load the output files
df_bert = pd.read_csv('sentiment_analysis_BERT.csv')
df_textblob = pd.read_csv('sentiment_analysis_textblob.csv')
df_vader = pd.read_csv('sentiment_analysis_VADER.csv')

# Descriptive statistics
stats_bert = df_bert['sentiment_score'].describe()
stats_textblob = df_textblob['sentiment_score'].describe()
stats_vader = df_vader['sentiment_score'].describe()

# Correlation analysis
correlation_matrix = pd.DataFrame({
    'BERT': df_bert['sentiment_score'],
    'TextBlob': df_textblob['sentiment_score'],
    'VADER': df_vader['sentiment_score']
})

correlation = correlation_matrix.corr()

# Print results
print("Descriptive Statistics:")
print("BERT:\n", stats_bert)
print("TextBlob:\n", stats_textblob)
print("VADER:\n", stats_vader)

print("\nCorrelation Matrix:")
print(correlation)
