import random

from word_frequency import histogram


def dict_sample(histogram):
    word_count = 0
    word_count += sum(hist[word] for word in hist.keys())
    word_range = 0
    histogram = {}
    random_int = random.random()

    for key in hist.keys():
        histogram[key] = hist[key] / word_count
        if word_range < random_int <= word_range + histogram[key]:
            return key
        word_range += histogram[key]


if __name__ == "__main__":
    filename = 'words.txt'

    word_histogram = {}

    with open(filename, 'r') as f:
        words = f.read().split(' ')
        hist = histogram(words)

    print(dict_sample(hist))
