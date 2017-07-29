from collections import Counter

n = int(raw_input())
a = map(int, raw_input().split())
c = Counter(a)

m = 0
for i in c:
    m = max(m, c[i] + c[i+1])
print m
