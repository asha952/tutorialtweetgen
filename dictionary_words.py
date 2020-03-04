import random
import sys as sys
from python_quote import random_python_quote


def random_sentence(sentence_len, words):
    sentence = ""
    for _ in range(sentence_len):
        word = random_python_quote(words)
        sentence += word + " "
    return sentence


if __name__ == "__main__":
    with open('words.txt', 'r') as f:
        words = f.read().split(' ')

    sentence_len = int(sys.argv[1])
    print(sentence_len)
    print(random_sentence(sentence_len, words))
