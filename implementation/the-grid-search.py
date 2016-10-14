
t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
        G_t = str(raw_input().strip())
        G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]

    P = []
    P_i = 0
    for P_i in xrange(r):
        P_t = str(raw_input().strip())
        P.append(P_t)

    check = False
    for r_index in xrange(len(G) - r + 1):
        for c_index in xrange(len(G[r_index]) - c):
            if G[r_index][c_index:c_index+c] == P[0]:
                check = True
                for i in xrange(1, len(P)):
                    if G[r_index + i][c_index:c_index+c] != P[i]:
                        check = False
                        break

                if check:
                    print 'YES'
                    break
        if check:
            break
    if not check:
        print 'NO'



