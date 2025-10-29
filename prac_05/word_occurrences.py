
words = {}
sentence = input("Text: ").lower()
sentence_split = sentence.split(" ")
max_length = max(len(word) for word in sentence_split)
for word in sentence_split:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

for word, number in sorted(words.items(), key = lambda item:item[0], reverse = False):
    print(f"{word: <{max_length}} : {number}")