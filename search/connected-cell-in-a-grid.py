

def FindOnes(coor):
    result = []

    for i in xrange(coor[0]-1, coor[0]+2):
        for j in xrange(coor[1]-1, coor[1]+2):
            if m > i >= 0 and n > j >= 0:
                if matrix[i][j]:
                    result.append((i,j))

    return result

def DFS(start):
    count = 0
    stack = FindOnes(start)

    for path in stack:
        if path not in visited:
            count += 1
            visited.append(path)

            for new in FindOnes(path):
                if new not in visited + stack:
                    stack.append(new)

    return count


if __name__ == '__main__':
    m = int(raw_input())
    n = int(raw_input())

    answer = 0
    matrix = []
    visited = []

    for r0 in xrange(m):
        row = map(int, raw_input().strip().split())
        matrix.append(row)

    for i in xrange(m):
        for j in xrange(n):
            if (i, j) not in visited:
                d = DFS((i,j))
                answer = max(answer, d)

    print answer


