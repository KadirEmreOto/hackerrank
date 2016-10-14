from itertools import combinations
from collections import defaultdict

def valid(x, y):
    if indices[x][0] > indices[y][0]: x, y = y, x

    if len(indices[x]) == len(indices[y]):
        check = True
        for i in xrange(len(indices[x])-1):
            if not indices[x][i] < indices[y][i] < indices[x][i+1]:
                check = False
                break

        if indices[x][-1] > indices[y][-1]:
            check = False

        if check: check = len(indices[x]) * 2
        return check

    if len(indices[x]) - 1 == len(indices[y]):
        check = True
        for i in xrange(len(indices[y])):
            if not indices[x][i] < indices[y][i] < indices[x][i+1]:
                check = False
                break

        if check: check = len(indices[x]) * 2 - 1
        return check
    return False

n = int(raw_input())
s = raw_input()

indices = defaultdict(list)

for i in xrange(n): indices[s[i]].append(i)

answer = 0
for i, j in combinations(indices.keys(), 2):
    answer = max(answer, valid(i, j))
print answer


