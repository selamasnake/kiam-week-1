import pandas as pd 
import seaborn as sns
import matplotlib.pylab as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator


def descriptive_statistics(data):
    headline_stats = data['headline'].describe()
    print(headline_stats)

    data['headline_length'] = data['headline'].apply(len)

    average_length = data['headline_length'].mode()[0] 
    print("Average Headline Length: ", average_length)

    length_range = data['headline_length'].max() - data['headline_length'].min()
    print("max: ",  data['headline_length'].max())
    print("min: ",  data['headline_length'].min())
    print("Headline Length Range: ", length_range)

def article_per_publisher(data):
    popular_publishers = data.groupby('publisher').size().sort_values(ascending=True)
    return popular_publishers

def analyze_publication_trends(data):
    publications_by_day = data['date'].dt.to_period('D').value_counts().sort_index()
    publications_by_month = data['date'].dt.to_period('M').value_counts().sort_index()
    publications_by_year = data['date'].dt.to_period('Y').value_counts().sort_index()

    # print("Publications by Year:")
    # print(publications_by_year)
    
    # print("\nPublications by Month:")
    # print(publications_by_month)
    
    # print("\nPublications by Day of the Month:")
    # print(publications_by_day)

    return publications_by_day, publications_by_month, publications_by_year

def analyze_publishing_time(data):
    data['publication_hour'] = data['date'].dt.hour
    publication_by_hour = data.groupby('publication_hour').size()
    print(publication_by_hour)
