with open('words', 'r') as f:
    text = f.read().lower()

words = text.split()

word_counts = {}

for word in words:
    word = word.strip('.,!?')
    if word in word_counts:
        word_counts[word] += 1 # {}
    else:
        word_counts[word] = 1
        #this 1
        #product 1+1 = 2

for word, count in word_counts.items():
    print(f"{word}: {count}")
