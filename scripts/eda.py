import pandas as pd 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def descriptive_statistics(data):
    headline_stats = data['headline'].describe()
    print(headline_stats)

    data['headline_length'] = data['headline'].apply(len)

    average_length = data['headline_length'].mode()[0] 
    print("Average Headline Length: ", average_length)

    length_range = data['headline_length'].max() - data['headline_length'].min()
    print("Headline Length Range: ", length_range)


def article_per_publisher(data):
    popular_publishers = data.groupby('publisher').size().sort_values(ascending=False)
    return popular_publishers

def analyze_publication_trends(data):
    publications_by_day = data['date'].dt.to_period('D').value_counts().sort_index()
    publications_by_month = data['date'].dt.to_period('M').value_counts().sort_index()
    publications_by_year = data['date'].dt.to_period('Y').value_counts().sort_index()

    print("Publications by Year:")
    print(publications_by_year)
    
    print("\nPublications by Month:")
    print(publications_by_month)
    
    # print("\nPublications by Day of the Month:")
    # print(publications_by_day)

## Text Analysis
def analyze_headline_sentiment(data):
    analyzer = SentimentIntensityAnalyzer()

    def classify_sentiment(compound_score):
        if compound_score >= 0.05:
            return 'positive'
        elif compound_score <= -0.05:
            return 'negative'
        else:
            return 'neutral'
    
    data['sentiment_score'] = data['headline'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
    data['sentiment'] = data['sentiment_score'].apply(classify_sentiment)
    
    return data

   




    
