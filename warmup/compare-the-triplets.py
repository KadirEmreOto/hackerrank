
a1, a2, a3 = map(int, raw_input().split())
b1, b2, b3 = map(int, raw_input().split())

s1 = (a1 > b1) + (a2 > b2) + (a3 > b3)
s2 = (a1 < b1) + (a2 < b2) + (a3 < b3)

print s1, s2


