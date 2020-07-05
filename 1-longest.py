from os import path
import wget

filename = "characters.bd2a09f6.txt"
if not path.exists(filename):
    url = "https://challenge.zuehlke.com/static/media/" + filename
    filename = wget.download(url)

f = open(filename, "r")
text = f.read()

for n in range(2, int(len(text)/2)):
    for offset in range(0,n):
        texti = text[offset : offset + n * int(len(text) / n)]
        list_substrings = [texti[i:i+n] for i in range(0, len(texti), n)]
        for substring in list_substrings:
            if (len(substring) > 2):
                number_of_occurrences = text.count(substring)
                if number_of_occurrences > 1:
                    biggest_substring = substring
                    break

print(biggest_substring)
