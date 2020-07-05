from os import path
import wget

salariesfile = "salary.c693064e.txt"
namesfile = "names.6020a082.txt"

for filename in [salariesfile, namesfile]:
    if not path.exists(filename):
        url = "https://challenge.zuehlke.com/static/media/" + filename
        filename = wget.download(url)


fs = open(salariesfile, "r")
salaries_text = fs.read()

fn = open(namesfile, "r")
names_text = fn.read()

names0 = []
for name in names_text.split(","):
    names0.append(name.strip())

salaries0 = []
for salary in salaries_text.split(","):
    salaries0.append(salary)

# We create a list with unique names and 
# another one with the full salary for each one:
names = []
salaries = []
for idx, name in enumerate(names0):
    if name not in names:
        names.append(name)
        salaries.append(int(salaries0[idx]))
    else:
        idx2 = names.index(name)
        salaries[idx2] = int(salaries[idx2]) + int(salaries0[idx])

max = salaries.index(max(salaries))
print(names[max])
