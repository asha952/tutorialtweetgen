import random
from random import shuffle
import sys as sys

# get the command line arguments with sys
if __name__ == "__main__":
    words = sys.argv[1:]
    shuffle(words)
    print(" ".join(words))
