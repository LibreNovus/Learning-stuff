string = ''
string = str(input())

list = []
sort = string.replace('+','')

for x in sort:
    list.append(x)

list.sort()

newstring = ''

for y in list:
    newstring = newstring + y
    newstring = newstring + '+'

print(newstring[:-1])

