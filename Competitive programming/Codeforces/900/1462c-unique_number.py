from sys import stdin,stdout
t = int(input())

for y in range(t):
    n = int(input())
    if n > 45:
        string = '-1'
        print(string)
        continue
    else:
        string = ''
        i = 9
        while i >= 1:
            if n <= 9 and n <= i:
                string += str(n)
                n = 0
                break
            else:
                string += str(i)
                n -= i
            i -= 1
    print(string[::-1])
