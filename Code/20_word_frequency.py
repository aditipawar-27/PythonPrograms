def word_frequency(sentence):
    frequency = {}
    words = sentence.lower().split()
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

if __name__ == "__main__":
    print(word_frequency("hello world hello"))
