from sys import stdin,stdout
n=int(stdin.readline())
sum = 0
for x in range(n):
    bit = str(raw_input())
    if bit == '++X' or bit == 'X++':
        sum += 1
    else:
        sum -= 1
print sum 
