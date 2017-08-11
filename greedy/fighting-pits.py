from collections import Counter

def add(team, strength):
    teams[team][0].append(strength)
    teams[team][1].append(teams[team][1][-1] + strength)

def query(x, y):
    x_cur = len(teams[x][0])
    y_cur = len(teams[y][0])

    turn = 0

    while True:
        if not turn:
            if teams[x][1][x_cur] >= teams[y][1][y_cur]:
                return x

            y_cur -= teams[x][0][x_cur-1]
            if y_cur <= 0:
                return x

        else:
            if teams[y][1][y_cur] >= teams[x][1][x_cur]:
                return y

            x_cur -= teams[y][0][y_cur-1]
            if x_cur <= 0:
                return y

        turn ^= 1

n, k, q = map(int, raw_input().split())
teams = [[[], [0]] for _ in xrange(k + 1)]

for s, t in sorted(map(int, raw_input().split()) for i in xrange(n)):
    add(t, s)

for i in xrange(1, k+1):
    teams[i][0].sort()

for i in xrange(q):
    c, x, y = map(int, raw_input().split())

    if c == 1:
        add(y, x)

    else:
        print query(x, y)

