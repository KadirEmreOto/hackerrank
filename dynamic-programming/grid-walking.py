def ways(d, offset, M):
    if M in mem[d] and offset in mem[d][M]:
        return mem[d][M][offset]

    val = 0
    if M == 0: val = 1
    
    else:
        if offset - 1 >= 1:
            val += ways(d, offset - 1, M - 1)
        if offset + 1 <= dimensions[d]:
            val += ways(d, offset + 1, M - 1)

    mem[d][M][offset] = val
    return val

def set_ways(left, right, M):
    if (left, right) in mem_set and M in mem_set[(left, right)]:
        return mem_set[(left, right)][M]
    if right - left == 1:
        return mem[left][M][origin[left]]

    val = 0
    split_point =  left + (right - left) / 2 
    for i in xrange(M + 1):
        t1 = i
        t2 = M - i
        mix_factor = fact[M] / (fact[t1] * fact[t2])
        val += mix_factor * set_ways(left, split_point, t1) * set_ways(split_point, right, t2)
    mem_set[(left, right)][M] = val
    return val

fact = [1]
for k in xrange(1, 301):
    fact.append(fact[-1] * k)

T = int(raw_input())
for ignore in xrange(T):
    N, M = map(int, raw_input().split())
    origin = map(int, raw_input().split())
    dimensions = map(int, raw_input().split())

    mem = {}
    for d in xrange(N):
        mem[d] = {}
        for i in xrange(M + 1):
            mem[d][i] = {}
            ways(d, origin[d], i)

    mem_set = {}
    for i in xrange(N + 1):
        for j in xrange(N + 1):
            mem_set[(i, j)] = {}
 
    answer = set_ways(0, N, M)
    print answer % 1000000007
