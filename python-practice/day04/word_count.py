sentence = input("Sentence: ").lower()

counts = {}
for word in sentence.split():
    counts[word] = counts.get(word, 0) + 1

for word, count in counts.items():
    print(f"{word}: {count}")
