from sys import setrecursionlimit; setrecursionlimit(10**6 + 4)

def split(number, limit=0, cur = []):
    if number == 0 and len(cur) != 1:
        yield cur

    if limit > number:
        return

    for i in xrange(limit + 1, number + 1):
        if 0 < number - i <= limit:
            continue

        for j in split(number-i, i, cur + [i]):
            yield j

def grundy(number):
    if number < 3:
        return 0

    if number in cache:
        return cache[number]

    acquired = set([])
    for j in split(number):
        acquired.add(solve(j))

    for i in xrange(len(acquired) + 1):
        if i not in acquired:
            cache[number] = i
            return i

def solve(array):
    a = 0
    for i in array:
        a ^= grundy(i)
    return a

cache = {}
for i in xrange(int(raw_input())):
    n = int(raw_input())
    print 'ALICE' if solve(map(int, raw_input().split())) else 'BOB'

