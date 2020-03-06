import random


def random_python_quote(lis):
    rand_index = random.randint(0, len(lis) - 1)
    return lis[rand_index]


if __name__ == '__main__':
    quotes = ["It's just a flesh wound.", "He's not the Messiah. He's a very naughty boy!", "THIS IS AN EX-PARROT!!"]

    quote = random_python_quote(quotes)
    print(quote)
