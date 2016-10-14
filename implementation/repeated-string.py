
s = raw_input()
n = int(raw_input())
a = s.count('a')
r = s[:n%len(s)].count('a')
print n / len(s) * a + r


