custom_sentence = input("Insert a phrase: ")
words = custom_sentence.split()

dictionary_sentence = {}

for word in words:
    dictionary_sentence[word] = len(word)

print(dictionary_sentence) 