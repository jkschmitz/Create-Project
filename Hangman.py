# Jake Schmitz
# CSCI 101 - Section E
# Python Lab 9
import math
import random


def get_word(diff):
    f = open("Words.txt", "r")
    words = f.read().split(",")
    word = ""
    if diff == 1:
        while len(word) > 6 or word == "":
            word = words[random.randint(0, len(words) - 1)]
    elif diff == 2:
        while len(word) < 6 or len(word) > 9:
            word = words[random.randint(0, len(words) - 1)]
    else:
        while len(word) < 8:
            word = words[random.randint(0, len(words) - 1)]
    f.close()
    return word


n = int(input("Input difficulty 1-3: "))
print(get_word(n))
# In later programming, ensure difficulty also changes how many guesses the user gets, not just the word length
