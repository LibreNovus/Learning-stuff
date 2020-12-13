n = int(input())
sum = 0
for i in range(n):
    s = raw_input()
    solver = 0
    for x in s:
        if x == '1':
            solver = solver +1
        else:
            continue
        if solver >= 2:
            sum = sum + 1
            break
print sum
