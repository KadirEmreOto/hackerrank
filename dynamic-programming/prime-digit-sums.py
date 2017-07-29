from collections import defaultdict

p = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43}
is_prime = lambda n: n in p

def ctrl(n1, n2):
    if n1 % 1000 != n2 // 10: return 0
    s = 0
    while n1:
        n1, r = divmod(n1, 10)
        s += r
    s += n2 % 10
    return is_prime(s)


mod = 10**9 + 7
dp = [[0]*(505) for i in range(2)]
frt = []
res = [0] * ((400001))
tr = defaultdict(list)

for x in range(10):
    for y in range(10):
        for z in range(10):
            if not is_prime(x + y + z):
                continue

            for k in range(10):
                if is_prime(x + y + z + k) and is_prime(y + z + k):
                    n = x*1000 + y*100 + z*10 + k
                    frt.append(n)

F = len(frt)
for i in range(F):
    if frt[i] >= 1000:
        dp[0][i] = 1
        res[4] += 1

    for j in range(F):
        if ctrl(frt[i], frt[j]):
            tr[i].append(j)
            #print i+1 , " - ", j + 1


for i in range(5, 400001):
    for j in range(0, F):
        if dp[0][j]:
            for it in tr[j]:
                dp[1][it] = (dp[1][it] + dp[0][j]) % mod
                res[i] = (res[i] + dp[0][j]) % mod

    for j in range(500):
        dp[0][j] = dp[1][j];3
        dp[1][j] = 0;

res[1] = 9
res[2] = 90
res[3] = 303

for _ in range(int(input())):
    n = int(input())

    print (res[n])


