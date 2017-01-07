
m = 10**9 + 7
n = int(raw_input())
a = map(int, raw_input().split())

pattern = []
pattern.append(pow(2, n, m) - 1)

for i in xrange((n-1) / 2):
    pattern.append(pattern[-1] + pow(2, n-2-i, m) - pow(2, i, m))

pattern += pattern[::-1]
if n & 1: del pattern[n/2]

answer = 0
for i in xrange(n):
    answer += a[i] * pattern[i]
    answer %= m

print answer

