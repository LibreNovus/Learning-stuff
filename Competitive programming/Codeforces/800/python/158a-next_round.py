from sys import stdin,stdout
n,k=map(int,stdin.readline().rstrip().split())

li = [int(x) for x in raw_input().split()]
passed = [x for x in li if (x>0 and x>=li[k-1])]
print len(passed)
