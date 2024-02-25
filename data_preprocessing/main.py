# Cleaning and Preprocessing Text Data in Pandas for NLP Tasks
import re
import pandas as pd
import nltk
nltk.download('stopwords')


if __name__ == "__main__":
    data = {'text': ["I love cooking!", "Baking is fun", None, "Japanese cuisine is great!"]}
    df = pd.DataFrame(data)
    print(df)
    df.dropna(subset=['text'], inplace=True)
    print(df)

    # Normalize text
    df['text'] = df['text'].str.lower()
    print(df)
    df['text'] = df['text'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
    print(df)

    # Tokenize text
    df['tokens'] = df['text'].str.split()
    print(df)

    # Remove Stop Words
    stop_words = set(stopwords.words('english'))
    df['tokens'] = df['tokens'].apply(lambda x: [word for word in x if word not in stop_words])
    print(df['tokens'])

    # Stemming and Lemmatization
    stemmer = PorterStemmer()
    df['stemmed'] = df['tokens'].apply(lambda x: [stemmer.stem(word) for word in x])
    print(df[['tokens', 'stemmed']])

    # Convert Text into Numerical Representations
    
