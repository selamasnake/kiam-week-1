import matplotlib.pyplot as plt
import seaborn as sns
from eda import analyze_publication_trends


def plot_publications_by_period(data):

    publications_by_day, publications_by_month, publications_by_year = analyze_publication_trends(data)
    publications_by_day_rolling = publications_by_day.rolling(window=7).mean()

    fig, axes = plt.subplots(3, 1, figsize=(12, 18))  

    sns.lineplot(x=publications_by_day_rolling.index.astype(str), y=publications_by_day_rolling.values, ax=axes[0], color='black')
    axes[0].set_title('Publications by Day')
    axes[0].set_xlabel('Day')
    axes[0].set_ylabel('Number of Publications')
    axes[0].tick_params(axis='x', rotation=45)


    sns.lineplot(x=publications_by_month.index.astype(str), y=publications_by_month.values, ax=axes[1], color='black')
    axes[1].set_title('Publications by Month')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Number of Publications')
    axes[1].tick_params(axis='x', rotation=45)

    sns.lineplot(x=publications_by_year.index.astype(str), y=publications_by_year.values, ax=axes[2], color='black')
    axes[2].set_title('Publications by Year')
    axes[2].set_xlabel('Year')
    axes[2].set_ylabel('Number of Publications')
    axes[2].tick_params(axis='x', rotation=45)

    # Adjust layout
    plt.tight_layout()
    plt.show()

def plot_publications_by_hour(data):
    data['publication_hour'] = data['date'].dt.hour
    publication_by_hour = data.groupby('publication_hour').size()

    plt.figure(figsize=(12, 12))
    sns.barplot(x=publication_by_hour.index, y= publication_by_hour.values, palette='Blues_d')

    plt.title('Publications by Hour of Day (Local Time)')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Publications')
    plt.xticks(rotation=0)
    plt.show()

#Stock Data

# def plot_stock_data( data):
#     fig = px.line(data, x=data.index, y=['Close', 'SMA'], title='Stock Price with Moving Average')
#     fig.show()

# def plot_rsi(data):
#     fig = px.line(data, x=data.index, y='RSI', title='Relative Strength Index (RSI)')
#     fig.show()

# def plot_ema(data):
#     fig = px.line(data, x=data.index, y=['Close', 'EMA'], title='Stock Price with Exponential Moving Average')
#     fig.show()

# def plot_macd(data):
#     fig = px.line(data, x=data.index, y=['MACD', 'MACD_Signal'], title='Moving Average Convergence Divergence (MACD)')
#     fig.show()

# def plot_daily_returns(data):
#     Ticker = ''
#     fig = px.line(data, x=data.index, y="Daily Returns", title=f"Daily Returns for {Ticker}")
#     fig.show()


#Plot Correlation

def plot_correlation(data):
    plt.figure(figsize=(8, 6))

    sns.scatterplot(x='sentiment_score', y='daily returns', data=data)

    # Adding title and labels
    plt.title('Sentiment Score vs Daily Returns')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Daily Returns')

    # Show the plot
    plt.show()
