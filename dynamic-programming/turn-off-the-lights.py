
N, K = map(int, raw_input().split())
C = map(int, raw_input().split())

if K > N:
    print min(C)
    quit()

ans = float('inf')
for i in xrange(K+1):
    t = 0
    for j in xrange(i, N, 2*K + 1):
        t += C[j]

    if j + K >= N-1:
        ans = min(ans, t)

print ans

