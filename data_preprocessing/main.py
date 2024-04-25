# Cleaning and Preprocessing Text Data in Pandas for NLP Tasks

import pandas as pd


if __name__ == "__main__":
    data = {'text': ["I love cooking!", "Baking is fun", None, "Japanese cuisine is great!"]}
    df = pd.DataFrame(data)
    print(df)
    df.dropna(subset=['text'], inplace=True)
    print(df)

    # Normalize text

