k,n,w = map(int,input().split())
sum = 0

for x in range(1, w+1):
    sum = sum + k*x

if sum - n > 0:
    print(sum - n)
else:
    print(0)
