## taking input from codeforces

## Method 1

a, b, c, d=[int(x) for x in input().split()]
print(a+b+c+d)

## Method 2
a, b, c, d=map(int,input().split())
print(a+b+c+d)

## Faster Methods 1
from sys import stdin, stdout
a,b,c,d=[int(x) for x in stdin.readline().rstrip().split()]
stdout.write(str(a+b+c+d)+'\n')

## Faster Method-2
from sys import stdin,stdout
a,b,c,d=map(int,stdin.readline().rstrip().split())
stdout.write(str(a+b+c+d)+'\n')

