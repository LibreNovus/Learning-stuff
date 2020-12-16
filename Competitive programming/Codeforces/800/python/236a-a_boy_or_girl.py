string = str(input())
le = len(''.join(set(string)))
if le % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')

