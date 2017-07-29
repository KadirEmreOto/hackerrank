from Queue import Queue
from collections import defaultdict

for _ in xrange(int(raw_input())):
    n, m = map(int, raw_input().split())
    graph = defaultdict(set)

    cost = [None] * (n+1)
    for i in xrange(m):
        u, v = map(int, raw_input().split())

        graph[u].add(v)
        graph[v].add(u)

    start = int(raw_input())
    queue = Queue()
    queue.put((start, 0))

    cost[start] = 0
    found = 1
    while not queue.empty() and found < n:
        node = queue.get()

        for i in xrange(1, n+1):
            if i not in graph[node[0]] and cost[i] == None:
                cost[i] = node[1] + 1
                queue.put((i, cost[i]))
                found += 1

    for i in cost:
        if i:
            print i,
    print

