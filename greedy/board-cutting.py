
mod = 10**9 + 7
T = int(raw_input())
for t in xrange(1, T+1):
    M, N = map(int, raw_input().split())
    cost1 = map(int, raw_input().split())
    cost2 = map(int, raw_input().split())

    segx = 1
    segy = 1

    sum1 = sum(cost1)
    sum2 = sum(cost2)

    cost1.sort()
    cost2.sort()

    i = M - 2
    j = N - 2


    answer = 0
    while i + j != -2:
        if i == -1:
#           print '1j', 'SegX', segx, 'SegY', segy
            answer += segx * cost2[j]; answer %= mod
            j -= 1; segy += 1; continue

        if j == -1:
#           print '2i', 'SegX', segx, 'SegY', segy
            answer += segy * cost1[i]; answer %= mod
            i -= 1; segx += 1; continue

        if cost1[i] > cost2[j]:
#           print '3i', 'SegX', segx, 'SegY', segy
            answer += segy * cost1[i]; answer %= mod
            i -= 1; segx += 1; continue

        elif cost1[i] < cost2[j]:
#           print '4j', 'SegX', segx, 'SegY', segy
            answer += segx * cost2[j]; answer %= mod
            j -= 1; segy += 1; continue

        else:
            if sum1 > sum2:
#               print '5i', 'SegX', segx, 'SegY', segy
                answer += segy * cost1[i]; answer %= mod
                i -= 1; segx += 1; continue

            else:
#               print '6j', 'SegX', segx, 'SegY', segy
                answer += segx * cost2[j]; answer %= mod
                j -= 1; segy += 1; continue
    print answer

