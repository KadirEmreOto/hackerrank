
N, K = map(int, raw_input().split())
A = map(int, raw_input().split())
S = set([])

for i in A:
    if i not in S and not N % i:
        S.add(i)

S = sorted(S)

if not S:
    print -1
    quit()

ks = [1]
dp = {1:1}
sp = {1:1}


for i in S:
    for j in ks:
        tmp = i * j
        ks.sort()
        if tmp > N:
            break

        ks.append(tmp)
        if tmp not in dp or (tmp in dp and sp[tmp] >= sp[j] + 1):
            sp[tmp] = sp[j] + 1
            dp[tmp] = i

if N not in dp:
    print -1
    quit()

ans = [1]
while N != 1:
    ans.append(N)
    N /= dp[N]

print ' '.join(map(str, sorted(ans)))

