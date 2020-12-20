from sys import stdin,stdout
t = int(input())

for y in range(t):
    x = int(input())
    sum = 0
    while (x != 0):
        sum = sum + x % 10
        x = x // 10
    print(sum)
