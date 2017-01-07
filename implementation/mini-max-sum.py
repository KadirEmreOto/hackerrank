a = map(int, raw_input().split())
a.sort()
print sum(a[:4]), sum(a[1:])
