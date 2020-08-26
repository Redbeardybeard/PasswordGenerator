import random
import math
import string
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


# global variables
# these variables are used to get the previously built password.
prev_word_mix = ''
prev_word_numb = ''
prev_word_punc = ''


random.seed()

# initiated tkinter
root = Tk()
#root.iconbitmap('/home/ortus/PycharmProjects/PasswordGenerator/icon.xbm')  <== not working fix later
root.title("password generator")


def get_dic_size(file):
    count = 0
    for l in file:
        count += 1
    return count


def find_word():
    with open('word_database.txt') as f:
        all_lines = f.readlines()
        ran = math.floor(random.random()*get_dic_size(all_lines))
        found_word = all_lines[ran].replace('\n', '')
        return found_word


def random_words():
    word_1 = find_word()
    word_2 = find_word()
    entry_1.delete(0,END)
    entry_2.delete(0,END)
    entry_1.insert(0,word_1)
    entry_2.insert(0, word_2)


#  see if you mix the following concat methods with lambda function
#  these methods work only for 2 words!


def concat(var):
    if var == "first-first":
        concat_ff()
    elif var == "first-last":
        concat_fl()
    elif var == "last-first":
        concat_lf()
    elif var == "last-last":
        concat_ll()


def concat_fl():  # first of first word, last of second word
    entry_generated_pass.delete(0, END)
    words = [entry_1.get(), entry_2.get()]
    ln1 = math.floor(len(words[0])/2)
    ln2 = math.floor(len(words[1]) / 2)
    txt = words[0][:ln1]+words[1][ln2:]
    entry_generated_pass.insert(0, txt)


def concat_lf():  # last of first word, first of second word
    entry_generated_pass.delete(0, END)
    words = [entry_1.get(), entry_2.get()]
    ln1 = math.floor(len(words[0])/2)
    ln2 = math.floor(len(words[1]) / 2)
    txt = words[0][ln1:]+words[1][:ln2]
    entry_generated_pass.insert(0, txt)


def concat_ff():
    entry_generated_pass.delete(0, END)
    words = [entry_1.get(), entry_2.get()]
    ln1 = math.floor(len(words[0])/2)
    ln2 = math.floor(len(words[1]) / 2)
    txt = words[0][:ln1]+words[1][:ln2]
    entry_generated_pass.insert(0, txt)


def concat_ll():
    entry_generated_pass.delete(0, END)
    words = [entry_1.get(), entry_2.get()]
    ln1 = math.floor(len(words[0])/2)
    ln2 = math.floor(len(words[1]) / 2)
    txt = words[0][ln1:]+words[1][ln2:]
    entry_generated_pass.insert(0, txt)


def mix_case():
    global prev_word_punc
    global prev_word_numb
    prev_word_punc = ''
    prev_word_numb = ''

    n_o_l = mix_case_entry.get()  # number of letters to be mix cased

    word = list(entry_generated_pass.get().lower())

    if n_o_l.isdigit():
        n_o_l = int(n_o_l)
    else:
        n_o_l = math.floor(len(word)*2/5)
        mix_case_entry.delete(0, END)
        mix_case_entry.insert(0, n_o_l)
    i = 0
    while i < n_o_l:
        random_character = random.randrange(0, len(word))  # feature or bug? sometimes same letters get picked
        word[random_character] = word[random_character].upper()
        i += 1
    joined_list = ""
    entry_generated_pass.delete(0, END)
    entry_generated_pass.insert(0, joined_list.join(word))


def numify():
    global prev_word_punc
    global prev_word_numb
    prev_word_punc = ''
    if prev_word_numb == '':
        prev_word_numb = entry_generated_pass.get()

    n_o_n = numify_entry.get()  # number of numbers to be added
    word = list(prev_word_numb)

    if n_o_n.isdigit():
        n_o_n = int(n_o_n)
    else:
        n_o_n = math.floor(len(word) * 2 / 5)
        numify_entry.delete(0, END)
        numify_entry.insert(0, n_o_n)

    i = 0
    while i < n_o_n:
        random_pos = random.randrange(0, len(word))
        word.insert(random_pos, str(random.randrange(0,10)))
        i += 1
    joined_list = ""
    entry_generated_pass.delete(0, END)
    entry_generated_pass.insert(0, joined_list.join(word))


def puncify():
    global prev_word_punc
    global prev_word_numb
    prev_word_numb = ''
    if prev_word_punc == '':
        prev_word_punc = entry_generated_pass.get()
    word = list(prev_word_punc)
    n_o_p = puncify_entry.get()

    if n_o_p.isdigit():
        n_o_p = int(n_o_p)
    else:
        n_o_p = math.floor(len(word)*2/5)
        puncify_entry.delete(0,END)
        puncify_entry.insert(0,n_o_p)

    i = 0
    puncs = string.punctuation
    punc_len = len(puncs)
    while i < n_o_p:
        random_pos = random.randrange(0,punc_len)
        word.insert(random_pos, str(puncs[random.randrange(0,punc_len)]))
        i += 1
    joined_list = ""
    entry_generated_pass.delete(0, END)
    entry_generated_pass.insert(0, joined_list.join(word))


# loading the image

img = ImageTk.PhotoImage(Image.open("lock.png"))
image_label = Label(image=img)

# defining tkinter widgets


label_frame_word = LabelFrame(root, text="Words", font="Helvetica")
label_e1 = Label(label_frame_word, text="First", font="Helvetica")
label_e2 = Label(label_frame_word, text="Second", font="Helvetica")
entry_1 = ttk.Entry(label_frame_word, width=20)
entry_2 = ttk.Entry(label_frame_word, width=20)
find_word_button = Button(label_frame_word, height=2, text="random words", font="Helvetica", command=random_words)


label_frame_config = LabelFrame(root, text="Config")
concat_Combo = ttk.Combobox(label_frame_config,state='readonly', width=9, font="Helvetica", values=["first-first", "first-last", "last-first", "last-last"])
concat_Combo.current(0)
concat_button = Button(label_frame_config, text="concat", font="Helvetica" ,command=lambda: concat(concat_Combo.get()))
mix_case_button = Button(label_frame_config, width=8, text="mix case", font="Helvetica", command=mix_case)
mix_case_entry = Entry(label_frame_config,width=5)
numify_button = Button(label_frame_config, width=8, text="mix number", font="Helvetica", command=numify)
numify_entry = Entry(label_frame_config,width=5)
puncify_button = Button(label_frame_config, width=8, text="mix symbols", font="Helvetica", command=puncify)
puncify_entry = Entry(label_frame_config,width=5)


label_frame_gp = LabelFrame(root, text="Generated Password", font="Helvetica",padx=50,pady=30)
entry_generated_pass = Entry(label_frame_gp, bd=3, relief=GROOVE)


# adding tkinter widgets to grid'


label_frame_word.grid(row=0, column=0, columnspan=2, padx=20, pady=5,stick=W)
label_e1.grid(row=0, column=0, padx=5, pady=5, stick=W)
label_e2.grid(row=1, column=0, padx=5, pady=5, stick=W)
entry_1.grid(row=0, column=1, padx=5)
entry_2.grid(row=1, column=1, padx=5)
find_word_button.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

image_label.grid(row=0, column=3)


label_frame_config.grid(row=1, column=0, padx=20,pady=5, stick=W)
concat_button.grid(row=0, column=1, padx=5, pady=2)
concat_Combo.grid(row=0, column=0, padx=5, pady=2)
numify_button.grid(row=2, column=0, padx=5, pady=5)
numify_entry.grid(row=2, column=1, padx=5, pady=5)
mix_case_button.grid(row=1, column=0, padx=5, pady=5)
mix_case_entry.grid(row=1, column=1, padx=5, pady=5)
puncify_button.grid(row=3, column=0, padx=5, pady=5)
puncify_entry.grid(row=3, column=1, padx=5, pady=5)


label_frame_gp.grid(row=1, column=1)
entry_generated_pass.grid(row=0, column=0)


root.mainloop()
