
def FindMax(i, j):
    down = FindDown(i, j)
    right = FindRight(i, j)

    ans = 0
    for c in xrange(right, 0, -1):
        d = FindDown(i, j + c)
        if d == -1: break

        if 2 * (c + N - i - 1) <= answer:
            break

        for r in xrange(min(down, d), 0, -1):
            l = FindLeft(i + r, j + c)
            if 2 * (c + r) < answer:
                break
            if l >= c:
                ans = max(ans, 2 * (r + c))
                break

    return ans

def FindLeft(i, j):
    if j < 0:
        return -1

    if matrix[i][j] == 'x':
        boundaries[i][j][0] = -1
        return -1

    if boundaries[i][j][0] != -2:
        return boundaries[i][j][0]

    left = FindLeft(i, j-1)

    boundaries[i][j][0] = left + 1
    return left + 1

def FindDown(i, j):
    if i >= N:
        return -1

    if matrix[i][j] == 'x':
        boundaries[i][j][1] = -1
        return -1

    if boundaries[i][j][1] != -2:
        return boundaries[i][j][1]

    down = FindDown(i+1, j)

    boundaries[i][j][1] = down + 1
    return down + 1

def FindRight(i, j):
    if j >= M:
        return -1

    if matrix[i][j] == 'x':
        boundaries[i][j][2] = -1
        return -1

    if boundaries[i][j][2] != -2:
        return boundaries[i][j][2]

    right = FindRight(i, j+1)

    boundaries[i][j][2] = right + 1
    return right + 1

N, M = map(int, raw_input().split())

matrix = []
for i in xrange(N):
    matrix.append(raw_input())

boundaries = [[[-2,-2, -2] for i in xrange(M)] for i in xrange(N)]

answer = 0
for i in xrange(N):
    for j in xrange(M):
        t = FindMax(i, j)

        #print('{}, {}: {}'.format(i, j, t))
        answer = max(answer , t)

if answer:
    print answer
else:
    print 'impossible'

