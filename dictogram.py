import random


class Dictogram:

    def __init__(self, word_list):

        self.word_list = word_list

        self.dictionary_histogram = self.build_dictogram()

        self.tokens = sum(self.dictionary_histogram.values())
        self.types = self.unique_words()

    def build_dictogram(self):
        histogram = {}
        for word in self.word_list:
            histogram[word] = histogram.get(word, 0) + 1
        return histogram

    def frequency(self, word):
        return self.dictionary_histogram.get(word, False)

    def unique_words(self):
        return len(self.dictionary_histogram)

    def sample(self):
        random_value = random.randrange(0, self.tokens)
        position = 0

        for key in self.dictionary_histogram.keys():
            position += self.dictionary_histogram[key]

            if position > random_value:
                return key

    def dictogram_samples(self, count):
        string = self.sample()

        for _ in range(count - 1):
            string += " " + self.sample()
        return string


def print_dictogram(word_list):
    print()
    print('Dictionary Histogram:')
    print('word list: {}'.format(word_list))
    dictogram = Dictogram(word_list)
    print('dictogram: {}'.format(dictogram.dictionary_histogram))
    print('{} tokens, {} types'.format(dictogram.tokens, dictogram.types))
    for word in word_list[-2:]:
        freq = dictogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_dictogram_samples(dictogram)


def print_dictogram_samples(dictogram):
    '''Compares sampled frequency to observed frequency'''

    print('Dictionary Histogram samples:')
    samples_list = [dictogram.sample() for _ in range(10000)]
    samples_hist = Dictogram(samples_list)
    print('samples: {}'.format(samples_hist.dictionary_histogram))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    for word, count in dictogram.dictionary_histogram.items():
        observed_freq = count / dictogram.tokens
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print('| {!r:<9} '.format(word)
              + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
              + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
              + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()


print_dictogram(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])
