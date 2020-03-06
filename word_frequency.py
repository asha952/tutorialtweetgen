def histogram(words):
    histogram = {}
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1
    return histogram


def list_histogram(words):
    list_words = get_pairs(words)
    histogram = []
    i = 0
    while i < len(list_words) - 1:
        list = []
        list.append(list_words[i])
        list.append(list_words[i + 1])
        histogram.append(list)
        i += 2
    return histogram


def get_pairs(words):
    pairs = []
    i = 0
    while len(words) > 0 and i < len(words):
        word = words[i]
        count = 1
        index = i + 1
        while index < len(words):
            if words[index] == word:
                count += 1
                words.pop(index)
                index = index - 1
            index += 1
        pairs.append(word.rstrip())
        pairs.append(count)
        # exit while loop
        i += 1
    return pairs


def unique_words(histogram):
    return len(histogram)


def frequency(histogram, word):
    return histogram.get(word, False)


if __name__ == "__main__":
    filename = 'words.txt'

    word_histogram = {}

    with open(filename, 'r') as f:
        words = f.read().split(' ')
    h = histogram(words)
    l = list_histogram(words)
    u = unique_words(h)
    f = frequency(h, 'yam')
    print(h)
    print(l)
    print(u, f)
