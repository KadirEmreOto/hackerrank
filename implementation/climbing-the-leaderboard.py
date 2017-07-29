from bisect import bisect

n = int(raw_input())
a = sorted(set(map(int, raw_input().split())))
q = int(raw_input())
t = map(int, raw_input().split())

n = len(a)
for i in t:
    print n -  bisect(a, i) + 1

