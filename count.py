def count_unique_words(filename):
    # your code here
    char_freq = {}
    with open(filename, 'r') as f:
        content = f.read()
        words = content.split()

        for word in words:
            if word in char_freq:
                char_freq[word] += 1
            else:
                char_freq[word] = 1

    top_words_list = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)[:10]
    for tup in top_words_list:
        word, freq = tup
        print(word, freq)


# count_unique_words()
if __name__ == '__main__':
    count_unique_words('hamlet.txt')
