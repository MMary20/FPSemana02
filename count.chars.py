custom_sentence = input("Insert a phrase: ")
words = custom_sentence.split()

dictionary = {}

for word in words:
    dictionary[word] = len(word)

print(dictionary) 