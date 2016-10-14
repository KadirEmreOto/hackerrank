
def PossiblePath(coordinate, previous=(-1,-1)):
    paths = []

    if coordinate[0] > 0:
        x, y = coordinate[0] - 1, coordinate[1]
        if matrix[x][y]: paths.append((x,y))

    if coordinate[0] < len(matrix) - 1:
        x, y = coordinate[0] + 1, coordinate[1]
        if matrix[x][y]: paths.append((x,y))

    if coordinate[1] > 0:
        x, y = coordinate[0], coordinate[1] - 1
        if matrix[x][y]: paths.append((x,y))

    if coordinate[1] < len(matrix[0]) - 1:
        x, y = coordinate[0], coordinate[1] + 1
        if matrix[x][y]: paths.append((x,y))

    if previous in paths:
        paths.remove(previous)

    return paths


def FindRotation(coordinate, previous=(-1,-1), count=0):
    pp = PossiblePath(coordinate, previous)
    

    if tuple(finish) in pp:
        if len(pp) > 1:
            return count + 1
        else:
            return count

    if len(pp) == 1:
        return FindRotation(pp[0], coordinate, count)

    elif len(pp) > 1:
        count += 1
        for p in pp:
            temp =  FindRotation(p, coordinate, count)
            if temp:
                return temp

start = tuple()
finish = tuple()

matris = []
case = int(raw_input().strip())

for c0 in range(case):
    t1, t2 = raw_input().strip().split(' ')

    matrix = []

    for r in xrange(int(t1)):
        row = raw_input().strip()

        temp = []
        for c in row:
            if c == '.':  c = 1
            elif c.lower() == 'x': c = 0

            if c == '*': finish = r, row.index(c)
            elif str(c).lower() == 'm': start = r, row.index(c)

            temp.append(c)
        matrix.append(temp)

    answer = int(raw_input().strip())
    if answer == FindRotation(start):
        print 'Impressed'
    else:
        print 'Oops!'
