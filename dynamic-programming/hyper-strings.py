from math import factorial
from collections import defaultdict

mod = 10**9 + 7

dp = {}
def solve(m):
    if m in dp: return dp[m]
    if m < 0: return 0
    if m == 0: return 1

    answer = 0
    for i in c:
        answer += i[1] * solve(m-i[0]) % mod

    dp[m] = answer % mod
    return dp[m]

def is_original(string, main):
    if not string: return False
    if string != main and string in superset: return False

    for i in superlist:
        if len(string) <= len(i): return True
        if string.startswith(i) and not is_original(string[len(i):], main):
            return False

N, M = map(int, raw_input().split())

superset = set([])
for i in xrange(N):
    string = raw_input()
    superset.add(string)

superlist = list(superset)
superlist.sort(key=lambda x: (len(x), x))

counter = defaultdict(int)

for string in superlist[:]:
    if is_original(string, string):
        counter[len(string)] += 1
    else:
        superlist.remove(string)
c = counter.items()
c.sort()
answer = 1
for i in xrange(1, M+1):
    answer += solve(i) % mod
print answer % mod

