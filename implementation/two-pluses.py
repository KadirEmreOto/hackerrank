
def getarea(grid, i, j):
    if grid[i][j] == ord('B'): return 0

    answer = min(n, m)

    k = i-1
    while k >= 0 and grid[k][j] != ord('B'): k -= 1
    answer = min(answer, i - k - 1)

    k = j-1
    while k >= 0 and grid[i][k] != ord('B'): k -= 1
    answer = min(answer, j - k - 1)

    k = i+1
    while k < n and grid[k][j] != ord('B'): k += 1
    answer = min(answer, k - i - 1)

    k = j+1
    while k < m and grid[i][k] != ord('B'): k += 1
    answer = min(answer, k - j - 1)

    return answer * 4 + 1

def fill(grid, i, j, size):
    grid[i][j] = ord('B')
    for k in xrange(1, size+1):
        grid[i+k][j] = ord('B')
        grid[i-k][j] = ord('B')
        grid[i][j+k] = ord('B')
        grid[i][j-k] = ord('B')

def empty(grid, i, j, size):
    grid[i][j] = ord('G')
    for k in xrange(1, size+1):
        grid[i+k][j] = ord('G')
        grid[i-k][j] = ord('G')
        grid[i][j+k] = ord('G')
        grid[i][j-k] = ord('G')


n, m = map(int, raw_input().split())
grid = [bytearray(raw_input()) for i in xrange(n)]

answer = 0
for i in xrange(n):
    for j in xrange(m):
        area = getarea(grid, i, j)
        size = (area - 1) / 4
        if not area: continue

        fill(grid, i, j, size)

        for x in xrange(n):
            for y in xrange(m):
                area2 = getarea(grid, x, y)
                answer = max(answer, area*area2)

        empty(grid, i, j, size)

print answer

