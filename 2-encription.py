# Use the Kasiski method to break a message cyphered using the Vigenère cypher. 

from os import path
import wget
import re
import numpy as np
import string
import matplotlib.pyplot as plt

filename = "crypto.204cfa7f.txt"
if not path.exists(filename):
    url = "https://challenge.zuehlke.com/static/media/" + filename
    filename = wget.download(url)

f = open(filename, "r")
text = f.read()

# Before decyphering the text, we make a copy:
list_dtext = [text[i] for i in range(0, len(text))]

# The alphabet in a list:
list_letters = list(string.ascii_uppercase)
# The most common letter in English:
index_E = list_letters.index('E')

# Compute how often any substring is repeated in the text:
dict0 = {}
for n in range(2, 20):
    for offset in range(0,n):
        texti = text[offset : offset + n * int(len(text) / n)]
        list_substrings = [texti[i:i+n] for i in range(0, len(texti), n)]
        for substring in list_substrings:
            if (len(substring) > 2):
                number_of_occurrences = text.count(substring)
                if number_of_occurrences > 1:
                    list_ocurrences = [m.start() for m in re.finditer(substring, text)]
                    #print(substring, list_ocurrences)
                    dict0[substring] = list_ocurrences

# Remove duplicates:
dict = {}
for key,value in dict0.items():
    if key not in dict.keys():
        dict[key] = value

# Print dictionary:
#for key in dict:
#    print(key, ' : ', dict[key])

def multiples (n):
    # Compute the multiples of an integer number
    lista = []
    for i in range(1,n+1):
        if n%i == 0:
            lista.append(i)
    return lista

# A ditionary is created in which all the multiples 
# are assigned to each key
dict2 = {}
for key,value in dict.items():
    list_multiples = []
    for i in value:
        for j in value:
            diff = j-i
            if diff > 0:
                list_multiples.append(multiples(diff))
    ll = [item for sublist in list_multiples for item in sublist]

    dict2[key] = list(set(ll))



# Print dictionary:
#for key in dict2:
#    print(key, ' : ', dict2[key])

def shift_letter (letter, shift):
    global list_letters
    index = list_letters.index(letter)
    newindex = (index + shift) % (len(list_letters))
    return list_letters[newindex]

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3

# A list of the common multiples for substrings longer than 4 characters:
list0 = range(0,100)
for key,value in dict2.items():
    if len(key) > 4:
        list0 = intersection (list0,value)

# The key can be of length 1, 2, 3, 4, 6 or 12.
#print(list0)
length_key = 12
list_key =[]

# Assuming a length of 12, we'll perform a frequency analysis
# of the letters at a distance of 12 apart. 
# These letters should follow the same frequency as in a normal English text.

fig, ax = plt.subplots(length_key, sharex=False, figsize=(4,8))

for n in range(0, length_key):
#for n in range(0, 1):
    x = [text[i+n] for i in range(0, len(text)-n, length_key)]
    labels, counts = np.unique(x,return_counts=True)


    #print(labels, counts)

    ticks = range(len(labels))
    plt.xticks(ticks, labels)
    ax[n].bar(ticks,counts, align='center')

    # The most frequent letter in English should be 'E', 
    # therefore we will perform a shift on the subgroup of letters:
    index_max = np.where(counts == np.amax(counts))[0][0]
    letter_max = labels[index_max]
    index_letter_max = list_letters.index(letter_max)
    shift = (index_E - index_letter_max) % (len(list_letters))
    list_key.append(list_letters[shift])

    # All the letters in the substring are shifted in the copy:
    for i in range(0, len(text)-n, length_key):
        list_dtext[i+n] = shift_letter (text[i+n], shift)

# Print frequencies:
#plt.show()


dtext = "".join(list_dtext)
#print(dtext)

key = "".join(list_key)
#print(key)

# This is the key I obtain from the method directly:
#key = "OQNQWCSIPENI"
# I recognized bits and pieces of words, 
# so I corrected the decyphering key by hand:
#key = "OMNQWCSIPENI"
key = "OMNQWCSIPANX"

def decypher (text,key):
    global list_letters
    #list_text = [text[i] for i in range(0, len(text))]
    dtext = ""
    for idx, letter in enumerate(text):
        shift_l = key[idx % len(key)]
        shift_n = list_letters.index(shift_l)
        #print(idx,letter)

        newletter = shift_letter(letter,shift_n)
        dtext = dtext + str(newletter)
    return dtext

decyphered_text = decypher (text,key)

for idx, letter in enumerate(decyphered_text):
    if idx%len(key)==0:
        line = decyphered_text[idx:idx+len(key)]
        #print(line)


# Now we have to calculate the cyphering key from the decyphering key we already have:
textA = "THENEFARIOUS"
textB = "FVRXIDIJTOHV"

key = ""
for idx, letterB in enumerate(textB):
    letterA = textA[idx]
    shift_n = (list_letters.index(letterB) - list_letters.index(letterA)) % len(list_letters)
    shift_l = list_letters[shift_n]
    key = key + shift_l


#key = "MONKEYISLAND"
print(key)
