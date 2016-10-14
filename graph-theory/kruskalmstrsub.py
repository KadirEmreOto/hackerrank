
class Kruskal(object):
    def __init__(self, nodes, edges):
        self.rank = {node: 0 for node in nodes}
        self.parent = {node: node for node in nodes}

        self.edges = edges      # [(node1, node2, cost), ] 

    def Solve(self):
        self.edges.sort(key=lambda x: x[2])

        answer = 0
        for x, y, r in self.edges:
            xroot = self.FindRoot(x)
            yroot = self.FindRoot(y)

            if xroot != yroot:
                self.Union(xroot, yroot)
                answer += r

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

if __name__ == '__main__':
    N, M = map(int, raw_input().split())

    nodes = xrange(1, N+1)
    edges = [map(int, raw_input().split()) for i in xrange(M)]

    kruskal = Kruskal(nodes, edges)
    print kruskal.Solve()
