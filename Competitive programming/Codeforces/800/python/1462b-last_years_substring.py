def solve(string, n):
    for i in range(0,5):
        s1 = string[0:i]
        s2 = string[n-4+i:]
        ans = s1+s2
        if ans == '2020':
            print('yes')
            return
    print('no')


c = int(input())

for x in range(c):
    n = int(input())
    s = str(input())
    solve(s, n)

