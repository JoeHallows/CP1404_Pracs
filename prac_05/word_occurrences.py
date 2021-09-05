

word_to_count = {}
text_to_count_words = str(input("Text: "))
words = text_to_count_words.split()
print(words)
for word in words:
    word_count = word_to_count.get(word, 0)
    word_to_count[word] = word_count + 1

words = list(word_to_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))

