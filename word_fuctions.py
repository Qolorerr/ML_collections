from ML_collections.pretext_check import pretext_check


# Tasks a, b, e
def most_frequent_rare_unique_words(data):
    all_words_dict = dict()
    for sentence in data:
        for word in sentence:
            if word in all_words_dict:
                all_words_dict[word] += 1
            else:
                all_words_dict[word] = 1
    sorted_data = sorted([[key, value] for key, value in all_words_dict.items()], key=lambda x: x[1], reverse=True)
    most_frequent = []
    index = 0
    while len(most_frequent) < 20:
        if not pretext_check(sorted_data[index][0]):
            most_frequent.append(sorted_data[index][0])
        index += 1
    return most_frequent, [item[0] for item in sorted_data[-20:]], len(all_words_dict)


# Task c
def longest_word(data):
    long_word = ""
    word_length = 0
    for sentence in data:
        for word in sentence:
            if len(word) > word_length:
                long_word = word
                word_length = len(word)
    return long_word


# Task d
def most_frequent_bigram(data):
    all_bigram_dict = dict()
    for sentence in data:
        if len(sentence) < 2:
            continue
        for i in range(len(sentence) - 1):
            bigram = sentence[i] + ' ' + sentence[i + 1]
            if bigram in all_bigram_dict:
                all_bigram_dict[bigram] += 1
            else:
                all_bigram_dict[bigram] = 1
    sorted_data = sorted([[key, value] for key, value in all_bigram_dict.items()], key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_data[:20]]


# Task f
def count_of_words(data):
    return sum([len(sentence) for sentence in data])
