# Cleaning and Preprocessing Text Data in Pandas for NLP Tasks
import re
import pandas as pd


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

