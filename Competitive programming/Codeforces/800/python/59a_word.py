n = str(input())
sum = 0
for i in n:
    if i.isupper() == True:
        sum = sum + 1
if sum > len(n)-sum:
    print(n.upper())
else:
    print(n.lower())
