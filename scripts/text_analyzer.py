from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from gensim import corpora
from gensim.models import LdaModel
import pyLDAvis.gensim_models
import spacy
nlp = spacy.load("en_core_web_sm")


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

def preprocess_text_spacy(data):
    processed_headlines = []

    # Use nlp.pipe for faster batch processing
    for doc in nlp.pipe(data['headline'].str.lower(), batch_size=1000, n_process=-1):
        # Lemmatize and remove stopwords and punctuation
        lemmatized_headline = ' '.join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])
        processed_headlines.append(lemmatized_headline)

    data['processed_headline'] = processed_headlines
    return data


def apply_lda(data):
    processed_headline = data['processed_headline'].apply(lambda x: x.split())
    dictionary = corpora.Dictionary(processed_headline)

    # Create the corpus (bag-of-words representation)
    corpus = [dictionary.doc2bow(text) for text in processed_headline]

    num_topics = 10

    # Train the LDA model using the corpus and dictionary
    lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)

    topics = lda_model.print_topics(num_words=5)
    for topic in topics:
        print(topic)
    
    pyLDAvis.enable_notebook(local=True)
    vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary)

    pyLDAvis.display(vis)

