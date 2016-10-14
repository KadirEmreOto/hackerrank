from copy import copy
from collections import defaultdict

N = int(raw_input())
S = raw_input()

dp = defaultdict(int)
dp2 = defaultdict(int)
dp3 = defaultdict(list)

rb = N
for i in xrange(N-1, -1, -1):
    if dp2[S[i]] < N / 4:
        dp3[S[i]].append(i)
        dp2[S[i]] += 1
        rb = min(i, rb)
    else:
        break

lb = 0
answer = rb

for i in S:
    if lb > rb: break

    if dp[i] < N / 4:
        dp[i] += 1

        if dp3[i] and dp2[i] == N / 4:
            temp = dp3[i].pop(-1)
            rb = max(rb, temp)

        elif dp2[i] < N / 4:
            dp2[i] += 1

        answer = min(answer ,rb - lb)
    else:
        break

    lb += 1

print answer

