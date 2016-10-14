import sys, resource, os
sys.setrecursionlimit(100005)

resource.setrlimit(resource.RLIMIT_STACK, (65532000, 65532000))


def dfs(nd, pre):
    sum_[nd-1] = arr[nd-1]
    
    for it in tree[nd]:
        if it != pre:
            sum_[nd-1] += dfs(it, nd)
    
    return sum_[nd-1]

def dfs2(nd, pre):
    global answer
    for it in tree[nd]:
        if it != pre:
            answer=min(answer, abs(sum_[0]-2*sum_[it-1]))
            dfs2(it, nd)

answer = 10**9

N = int(raw_input().strip())
arr = map(int, raw_input().strip().split())

sum_ = [0]*N
tree = {}
binary = []
for i in xrange(N-1):
    T1 , T2 = map(int, raw_input().strip().split())
    binary.append((T1, T2))
    if T1 in tree:
        if T2 not in tree[T1]:
            tree[T1].append(T2)
    else:
        tree[T1] = [T2]

    if T2 in tree:
        if T1 not in tree[T2]:
            tree[T2].append(T1)
    else:
        tree[T2] = [T1]

dfs(1, 0)
dfs2(1, 0)
print answer
