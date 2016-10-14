



if __name__ == '__main__':
    N = 800
    MAXN = 10**5

    s = [0] * 1000
    nxt = [[-1] * 10 for i in xrange(MAXN)]
    cut =  [-1] * MAXN
    state = [[-1] * 305 for i in xrange(1000)]
    val = [bytearray(' '*305) for i in xrange(1000)]
    w = [0] * MAXN
    u = [0] * MAXN

    m = 1
    n = 1
    s[0] = 1
    for i in xrange(N+1):
        pos = 0
        for j in xrange(n):
            if nxt[pos][s[j]] == -1:
                nxt[pos][s[j]] = m
                m += 1
            pos = nxt[pos][s[j]]
            state[i][j] = pos
            val[i][j] = s[j]

        for j in xrange(n): s[j] <<= 1
        for j in xrange(n):
            if s[j] >= 10:
                s[j+1] += s[j]/10
                s[j] %= 10

        n += (s[n]>0)

    cut[0] = 0
    for j in xrange(n):
        for i in xrange(N+1):
            pos = state[i][j]
            if pos == -1 or u[pos]:
                continue
            u[pos] = 1
            if j == 0:
                cut[pos] = 0
            else:
                k = cut[state[i][j-1]]
                while k and nxt[k][val[i][j]] == -1:
                    k = cut[k]
                cut[pos] = max(nxt[k][val[i][j]], 0)
            w[pos] = w[cut[pos]] + (state[i][j+1] == -1)

    T = int(raw_input())
    for t_ in xrange(T):
        r = raw_input()[::-1]
        pos = 0
        ans = 0

        for i in xrange(len(r)):
            t = int(r[i])
            while pos and nxt[pos][t] == -1:
                pos = cut[pos]
            pos = max(0, nxt[pos][t])
            ans += w[pos]
        print ans

