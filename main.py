import random
import math
import string

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
        rcw.append(all_lines[ran].replace('\n', ''))
        return rcw

#  see if you mix the following concat methods with lambda function
#  these methods work only for 2 words!


def concat_fl(words):  # first of first word, last of second word
    ln1 = math.floor(len(words[0])/2)
    ln2 = math.floor(len(words[1]) / 2)
    txt = words[0][:ln1]+words[1][ln2:]
    return txt


def concat_lf(words):  # last of first word, first of second word
    ln1 = math.floor(len(words[0])/2)
    ln2 = math.floor(len(words[1]) / 2)
    txt = words[0][ln1:]+words[1][:ln2]
    return txt


def concat_ff(words):
    ln1 = math.floor(len(words[0])/2)
    ln2 = math.floor(len(words[1]) / 2)
    txt = words[0][:ln1]+words[1][:ln2]
    return txt


def concat_ll(words):
    ln1 = math.floor(len(words[0])/2)
    ln2 = math.floor(len(words[1]) / 2)
    txt = words[0][ln1:]+words[1][ln2:]
    return txt


def mix_case(word):
    word = word.lower()
    word = list(word)
    i = 0
    count = math.floor(len(word)*2/5)  # debatable number of case switches
    while i < count:
        random_character = random.randrange(0, len(word)-1)
        word[random_character] = word[random_character].upper()
        i += 1
    joined_list = ""
    return joined_list.join(word)


def numify(word):
    word = list(word)
    i = 0
    count = math.floor(len(word)*1/3)  # 1/3 is debatable...
    while i < count:
        random_pos = random.randrange(0,len(word)-1)
        word.insert(random_pos,str(random.randrange(0,10)))
        i += 1
    joined_list = ""
    return joined_list.join(word)


def puncify(word):
    word = list(word)
    i = 0
    count = math.floor(len(word)*2/5)
    puncs = string.punctuation
    punc_len = len(puncs)
    while i < count:
        random_pos = random.randrange(0,punc_len-1)
        word.insert(random_pos, str(puncs[random.randrange(0,punc_len-1)]))
        i += 1
    joined_list = ""
    return joined_list.join(word)


find_word(randomly_chosen_words)
find_word(randomly_chosen_words)


print("the chosen words ", randomly_chosen_words)

next_step = concat_ff(randomly_chosen_words)
print("concated: ", next_step)

next_step = mix_case(next_step)
print("mix cased: ", next_step)

next_step = numify(next_step)
print("added numbers: ", next_step)

next_step = puncify(next_step)
print("added punctuations: ", next_step)

