from Queue import Queue
from collections import defaultdict

class Kruskal(object):
    def __init__(self, nodes, edges):
        self.rank = {node: 0 for node in nodes}
        self.parent = {node: node for node in nodes}

        self.edges = edges
        self.tree = defaultdict(list)

    def Solve(self):
        self.edges.sort(key=lambda x: x[2])

        answer = 0
        for x, y, r in self.edges:
            xroot = self.FindRoot(x)
            yroot = self.FindRoot(y)

            if xroot != yroot:
                self.Union(xroot, yroot)
                answer += r
                self.tree[x].append((y, r))
                self.tree[y].append((x, r))

        return answer

    def FindRoot(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.FindRoot(self.parent[node])

        return self.parent[node]

    def Union(self, xroot, yroot):
        if self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = self.parent[xroot]

        else:
            self.parent[xroot] = self.parent[yroot]

            if self.rank[xroot] == self.rank[yroot]:
                self.rank[yroot] += 1

def DFS(node, pre):
    for it in kruskal.tree[node]:
        if it[0] != pre:
            dp[node] += DFS(it[0], node) + 1

    return dp[node]

n, m = map(int, raw_input().split())
edges = [map(int, raw_input().split()) for i in xrange(m)]
kruskal = Kruskal(range(1, n+1), edges)
kruskal.Solve()

dp = [0] * (n + 1)
DFS(1, 0)

queue = Queue()
queue.put((1, 0, 0))

answer = 0
while not queue.empty():
    node = queue.get()

    if node[1] != 0:
        answer += (dp[node[0]]+1) * (n - dp[node[0]]-1) * (2**node[2])

    for it in kruskal.tree[node[0]]:
        if it[0] != node[1]:
            queue.put((it[0], node[0], it[1]))
print bin(answer)[2:]

