def sum(n):
    return (n*(n+1))//2


for _ in range(int(raw_input())):
    n,k,b = map(int, raw_input().split())
    if sum(k) - sum(k-b) < n or sum(b) > n:
        print(-1)
    else:
        s = sum(b)
        res = [0] * b
        for i in range(b):
            res[i] = i+1
        if s == n:
            for i in res:
                print i,
            print
        else:
            lim = k
            for i in range(len(res)-1,-1,-1):
                if n == s:
                    break
                elif n >= s+lim-res[i]:
                    s += lim-res[i]
                    res[i] = lim
                    lim -= 1
                else:
                    res[i] += n-s
                    s = n
            for i in res:
                print i,
            print

