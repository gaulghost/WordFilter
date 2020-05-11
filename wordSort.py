import re

user = input("enter the file name\n")
fhand = open(user)

lst1 = list(range(65,91))
lst2 = list(range(97,123))
flst = lst1 + lst2

validword2 = list()
strings = list()
invalidword = list()
validword = list()

for line in fhand :
    line = line.rstrip()
    x = re.findall('\s([a-zA-Z]+)\.\s', line)
    y = re.findall('\s([a-zA-Z]+),\s', line)
    z = re.findall('([a-zA-Z]+),\s', line)
    w = re.findall('([a-zA-Z]+)\.\s', line)
    if x is not None :
        for word in x:
            validword2.append(word)
    if y is not None :
        for word in y:
            validword2.append(word)
    if z is not None :
        for word in z:
            validword2.append(word)
    if w is not None :
        for word in w:
            validword2.append(word)
    line = line.split()
    for word in line :
        strings.append(word)

for string in strings :
    for letter in string :
        if ord(letter) not in flst :
            invalidword.append(string)

validword = set(strings)-set(invalidword)

for word in validword2 :
        validword.add(word)

print(validword)
print(len(validword))
