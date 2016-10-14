from sys import setrecursionlimit, maxint
import resource

resource.setrlimit(resource.RLIMIT_STACK, (65000000, 65000000))
setrecursionlimit(10**5+4)

def Solve(i=0):
    if dp[i]: return dp[i]
    if i + K >= N: return array[i]

    answer = maxint
    minimum = maxint

    for j in xrange(K+1, 0, -1):
        if array[i + j] < minimum:
            answer = min(answer, array[i] + Solve(i + j))
            minimum = array[i+j]

    dp[i] = answer
    return answer

N, K = map(int, raw_input().split())

dp = [0] * (N+3)
total = 0
array = [0]

for i in xrange(N):
    array.append(int(raw_input()))
    total += array[-1]

print total - Solve()

