

def DFS(start, pre=0):
    global answer
    count = 0

    childs = tree[start][:]
    tree[start] = 1

    for i in childs:
        if i != pre:
            tree[start] += DFS(i, start)

    if not tree[start] % 2: answer += 1
    if len(childs) == 1:
        return 1
    return tree[start]

if __name__ == '__main__':
    N, M = map(int, raw_input().split())

    tree = {}
    for m0 in xrange(M):
        a, b = map(int, raw_input().split())

        if a not in tree: tree[a] = [b]
        elif b not in tree[a]: tree[a].append(b)

        if b not in tree: tree[b] = [a]
        elif a not in tree[b]: tree[b].append(a)


    answer = 0
    DFS(1, 0)
    print answer - 1

