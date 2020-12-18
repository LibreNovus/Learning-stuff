from sys import stdin,stdout
n,k=map(int,stdin.readline().rstrip().split())

string = str(n)
for x in range(k):
    if string[-1] == '0':
        n = n / 10
        string = str(int(n))
    else:
        n = n - 1
        string = str(int(n))
print(string)
