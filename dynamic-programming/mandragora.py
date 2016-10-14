
T = int(raw_input())

for t in xrange(T):
    N = int(raw_input())
    array = map(int, raw_input().split())
    array.sort()

    dp = [0]
    for it in array:
        dp.append(dp[-1] + it)

    answer = 0
    for i in xrange(N):
        s = i + 1
        p = dp[N] - dp[i]
        answer = max(s*p, answer)
    print answer
        
