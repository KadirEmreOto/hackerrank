from bisect import bisect

def BFS(start):
    try:
        queue = tree[start][:]
    except:
        return None
    visited = [start]

    last = 1
    index = 0
    count = [len(queue), len(queue)]

    while queue:
        node = queue.pop(0)

        if (bisect(count, index) + 1) > last:
            last += 1
            count.append(count[-1])

        visited.append(node)
        for n in tree[node]:
            if n not in queue + visited:
                queue.append(n)
                count[-1] += 1


        result[node-1] = (bisect(count, index) + 1) * 6
        index += 1


if __name__ == '__main__':
    T = int(raw_input())

    for t0 in xrange(T):
        N, M = map(int, raw_input().split())

        tree = {}
        result = [-1] * N 

        for m0 in xrange(M):
            x, y = map(int, raw_input().split())
            
            if x not in tree: tree[x] = [y]
            elif y not in tree[x]: tree[x].append(y)

            if y not in tree: tree[y] = [x]
            elif x not in tree[y]: tree[y].append(x)

        start = int(raw_input())
        result[start - 1] = 0


        BFS(start)
        for i in result:
            if i != 0:
                print i,
        print

