from flask import Flask

from dictionary_words import random_sentence

app = Flask(__name__)


@app.route('/')
def generate_words():
    with open('words.txt', 'r') as f:
        words = f.read().split(' ')

    return random_sentence(5, words)


if __name__ == '__main__':
    app.run()
