words = ["apple", "banana", "apple", "orange", "banana", "apple"]

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

for word in frequency:
    print(word, ":", frequency[word])
