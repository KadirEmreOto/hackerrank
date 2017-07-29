
n = int(raw_input())

a = set(map(int, raw_input().split()))

while True:
    m = max(a)

    if m == 0:
        print 0
        quit()

    i = -1
    while m:
        m >>= 1
        i += 1


    m = 1 << i
    l = set(filter(lambda x: x & m, a))
    r = a.difference(l)

    if r: break
    a = set(map(lambda x: x ^ m, a))

ans = float('inf')
for i in l:
    for j in r:
        ans = min(ans, i ^ j)

print ans

