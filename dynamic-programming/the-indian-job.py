
def Solve(i=0, l=0, r=0):
    if i in dp and l in dp[i] and r in dp[i][l]:
        return dp[i][l][r]

    if l > g or r > g: return False
    if i == n: return True

    answer = Solve(i+1, l+a[i], r) or Solve(i+1, l, r+a[i])

    if i not in dp: dp[i] = {}
    if l not in dp[i]: dp[i][l] = {}
    dp[i][l][r] = answer
    return answer

T = int(raw_input())

for t in xrange(T):
    n, g = map(int, raw_input().split())
    a = map(int, raw_input().split())
    dp = {}

    if Solve(): print 'YES'
    else: print 'NO'

