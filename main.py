import random
import math

random.seed()
randomly_chosen_words = []


def get_dic_size(file):
    count = 0
    for l in file:
        count += 1
    return count


def find_word(rcw):
    with open('word_database.txt') as f:
        all_lines = f.readlines()
        ran = math.floor(random.random()*get_dic_size(all_lines))
        rcw.append(all_lines[ran])
        return rcw


find_word(randomly_chosen_words)
find_word(randomly_chosen_words)
find_word(randomly_chosen_words)
print(randomly_chosen_words)


