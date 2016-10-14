from sys import maxint as inf
from collections import defaultdict

N = int(raw_input())
array = map(int, raw_input().split())
dp = defaultdict(list)

for i in xrange(N):
    dp[array[i]].append(i)

answer = inf
for n in dp:
    for i in xrange(len(dp[n])-1):
        answer = min(answer, dp[n][i+1] - dp[n][i])
if answer == inf:
    print -1
else:
    print answer
        
        




