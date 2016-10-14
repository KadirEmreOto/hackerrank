#-*- coding: UTF-8 -*-
from bisect import bisect

def BFS(start):
    queue = tree[start][:]

    visited = [0] * 101
    result = [-1] * 101
    visited[1] = 1

    last = 1
    index = 0
    count = [len(queue), len(queue)]

    while queue:
        node = queue.pop(0)

        if (bisect(count, index) + 1) > last:
            last += 1
            count.append(count[-1])

        visited[node] = 1
        for n in tree[node]:
            if n not in queue and not visited[n]:
                queue.append(n)
                count[-1] += 1


        result[node] = (bisect(count, index) + 1) 
        index += 1

    return result[-1]

if __name__ == '__main__':
    T = int(raw_input())

    for _ in xrange(T):
        tree = {i: range(i+1, i+7) for i in xrange(1, 95)}
        tree.update({i: range(i+1, 101) for i in xrange(95, 100)})
        tree[100] = []

        L = int(raw_input())
        for _ in xrange(L):
            x, y = map(int, raw_input().split())

            del tree[x]
            for i in xrange(x-6, x):
                if i in tree:
                    tree[i][x-i-1] = y

        S = int(raw_input())
        for _ in xrange(S):
            x, y = map(int, raw_input().split())

            del tree[x]
            for i in xrange(x-6, x):
                if i in tree:
                    tree[i][x-i-1] = y

        print BFS(1)
