
def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1


N, M = map(int, raw_input().split())

rank = {}
parent = dict()
edges = []

for i in xrange(1, N+1):
    rank[i] = 0
    parent[i] = i

for _ in xrange(M):
    edge = map(int, raw_input().split())
    edges.append(edge)

start = int(raw_input())
edges.sort(key=lambda x: x[2])

ans = 0
for edge in edges:
    x, y, r = edge

    if find(x) != find(y):
        union(x, y)
        ans += r

print ans
