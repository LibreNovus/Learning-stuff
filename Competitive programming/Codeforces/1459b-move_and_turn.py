n = int(input())
steps = int(n/2)
if n % 2 == 0:
    print(int(((n/2)+1)**2))
    steps -= 1
else:
    print(2*(steps + 1)*(steps + 2))

