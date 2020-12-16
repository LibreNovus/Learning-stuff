n = int(input())
string = str(input())
sum = 0
for x in range(len(string)-1):
    if string[x] == string[x+1]:
        sum += 1
print(sum)

