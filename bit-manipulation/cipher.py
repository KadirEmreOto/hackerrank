
N, K = map(int, raw_input().split())
numb = raw_input()

one = 0
ans = ''

for i in xrange(N):
    n = numb[i]
    
    if (K <= i and ans[i-K] == '1'):
        one -= 1

    if n == '1' and not one % 2:
        ans += '1'
        one += 1

    elif n == '1' and one % 2:
        ans += '0'

    elif n == '0' and not one % 2:
        ans += '0'

    else:
        ans += '1'
        one += 1

print ans
