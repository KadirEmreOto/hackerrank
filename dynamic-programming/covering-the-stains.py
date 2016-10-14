# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT

mod = 1000000007
N, K = map(int, raw_input().split())
l = []
for i in xrange(N):
    a,b = map(int, raw_input().split())
    l.append((a,b))

limits = []
# xmin
xmin = min([x[0] for x in l])
limits.append(set([i for i in xrange(len(l)) if l[i][0] == xmin]))

#xmax
xmax = max([x[0] for x in l])
limits.append(set([i for i in xrange(len(l)) if l[i][0] == xmax]))

#ymin
ymin = min([x[1] for x in l])
limits.append(set([i for i in xrange(len(l)) if l[i][1] == ymin]))

#ymax
ymax = max([x[1] for x in l])
limits.append(set([i for i in xrange(len(l)) if l[i][1] == ymax]))

fact = [1]
for i in xrange(1,2000):
    fact.append((i*fact[-1]) % mod)
              
def inv(x):
    return pow(x, mod-2, mod)
              
def comb(a, b):
    return (fact[a] * inv(fact[b]) * inv(fact[a-b])) % mod
              
ans = 0
for i in xrange(1, 16):
    temp = set([])
    cnt = 0
    for j in xrange(4):
        if (i / (2**j)) % 2 == 1:
            cnt += 1
            temp = temp.union(limits[j])
    if len(temp) > K: continue
    tmp = comb(N - len(temp), K - len(temp))
    if cnt % 2 == 0: ans = (ans - tmp + mod) % mod
    else: ans = (ans + tmp) % mod

print ans

