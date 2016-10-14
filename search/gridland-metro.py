from bisect import bisect
from collections import defaultdict

n, m, k = map(int, raw_input().split())
rows = defaultdict(list)

for i in xrange(k):
    r, c1, c2 = map(int, raw_input().split()); c2 += 1
    if not rows[r]: rows[r].append([c1, c2]); continue

    left = bisect(rows[r], [c1, float('inf')])
    right = bisect(rows[r], [c2, float('inf')])

    if left and c1 <= rows[r][left-1][1]:
        rows[r][left-1][1] = max(rows[r][left-1][1], rows[r][right-1][1], c2)
        del rows[r][left:right]

    elif c1 > rows[r][left-1][1]:
        cm = rows[r][right-1][1]
        del rows[r][left:right]
        rows[r].insert(left, [c1, max(cm, c2)])

    else:
        if not right:
            rows[r].insert(0, [c1, c2])

        else:
            cm = rows[r][right-1][1]
            del rows[r][left:right]
            rows[r].insert(0 ,[c1, max(cm, c2)])

answer = n*m

for i in rows:
    for j in rows[i]:
        answer -= j[1] - j[0]

print answer

