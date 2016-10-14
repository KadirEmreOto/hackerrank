from copy import copy

cache = {}

def Solve(n, p, used):
    t = tuple(used)
    if n in cache and p in cache[n] and t in cache[n][p]:
        return cache[n][p][t]

    if p == N-1: return array[n][p]

    cur = array[n][p]
    ans = Solve(n, p+1, used)

    for i in xrange(M):
        u = copy(used)
        u.add(n)
        if i not in used:
            ans = min(ans, Solve(i, p+1, u))

    #print n, p, t, '-->', cur + ans
    if n not in cache: cache[n] = {}
    if p not in cache[n]: cache[n][p] = {}
    cache[n][p][t] = cur + ans
    return cache[n][p][t]



N, M = map(int, raw_input().split())

array = []
for m in xrange(M):
    array.append(map(int, raw_input().split()))

answer = sum(array[0])
for n in xrange(M):
    answer = min(answer, Solve(n, 0, set([])))
print answer

