n = int(input())
ontrain = 0
sum =0
for x in range(n):
    a,b = map(int, input().split())
    ontrain += b
    ontrain -= a
    if ontrain>sum:
        sum = ontrain
print(sum)
