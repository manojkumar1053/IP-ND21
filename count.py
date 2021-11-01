def count_unique_words(filename):
    # your code here
    char_freq = {}
    with open(filename, 'r') as f:
        content = f.read()
        words = content.split()

        # Method 1 to create the word freq list
        # for word in words:
        #     if word in char_freq:
        #         char_freq[word] += 1
        #     else:
        #         char_freq[word] = 1

        # Method 2 create the word freq list
        for word in words:
            char_freq[word] = char_freq.get(word, 0) + 1

    # Sort the dict baaed on the value and then get the top 10 values
    top_words_list = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)[:10]
    for tup in top_words_list:
        word, freq = tup
        print(word, freq)


# count_unique_words()
if __name__ == '__main__':
    count_unique_words('hamlet.txt')
