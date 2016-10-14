from collections import Counter

N, H, I = map(int, raw_input().split())

floors = [[]]
for n in xrange(N):
    array = map(int, raw_input().split())
    floors.append(Counter(array[1:]))

dp = [[0]* (H+4) for i in xrange(N+4)]
mh = [0] * (H+4)

for f in xrange(1, H+1):
    for b in xrange(1, N+1):
        dp[b][f] = dp[b][f-1]
        if f - I > 0:
            dp[b][f] = max(dp[b][f], mh[f-I])
        dp[b][f] += floors[b][f]
        mh[f] = max(mh[f], dp[b][f])

answer = 0
for b in xrange(1, N+1):
    answer = max(answer, dp[b][H])
print answer

