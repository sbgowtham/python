import pandas as pd
from collections import Counter

df = pd.read_csv('reviews.csv')

all_words = (' '.join(df['review'])
             .lower().split())

word_counts = Counter(all_words)

print(word_counts.most_common(1))
