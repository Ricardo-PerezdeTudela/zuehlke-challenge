from os import path
import wget
import tabula

filename = "scroll.3ecebd1a.pdf"

if not path.exists(filename):
    url = "https://challenge.zuehlke.com/static/media/" + filename
    file = wget.download(url)

table = tabula.read_pdf(filename, pandas_options={'header': None, 'squeeze':True})

numbers = []
for line in table:
    x = [int(s) for s in str(line) if s.isdigit()]
    numbers.append(x)

# flatten and convert into characters:
numbers = [item for sublist in numbers for item in sublist]
numbers = [str(integer) for integer in numbers]

chunk1 = "".join(numbers[:7])
chunk2 = "".join(numbers[7:])

coord1 = chunk1[0:2] + "." + chunk1[2:4] + "." + chunk1[4:6] + "." + chunk1[6] + "N"
coord2 = chunk2[0:2] + "." + chunk2[2:4] + "." + chunk2[4:6] + "." + chunk2[6] + "W"

coordinates = coord1 + " " + coord2

print(coordinates)

#17.38.38.5N 63.15.10.0W
