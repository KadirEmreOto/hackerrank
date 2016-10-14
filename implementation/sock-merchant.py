from collections import Counter

n = int(raw_input())
a = map(int, raw_input().split())
c = Counter(a)

ans = 0
for i in c:
    ans += (c[i]>>1)
print ans


