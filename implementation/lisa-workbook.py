

N, K = map(int, raw_input().split())
arr = map(int, raw_input().split())

ans = 0
page = 0
for c in arr:
    page += 1
    for i in xrange(1, c+1):
        if i == page:
            ans += 1

        if not i % K and i != c:
            page += 1
print ans
