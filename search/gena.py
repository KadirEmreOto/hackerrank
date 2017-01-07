from collections import deque

def lsb(a):
    r = 1
    while r <= a:
        if r & a: return r
        r <<= 1

def bfs(node):
    used = set()

    queue = deque()
    queue.append((tuple(node), 0))

    while queue:
        node, answer = queue.popleft()

        if node[0] == (1 << n) - 1:
            return answer

        for i in xrange(4):
            for j in xrange(4):
                if node[i] and (not node[j] or lsb(node[i]) < lsb(node[j])):
                    child = list(node)
                    child[i] ^= lsb(node[i])
                    child[j] ^= lsb(node[i])
                    child[1:4] = sorted(child[1:4], key=lsb)
                    child = tuple(child)
                    if not child in used:
                        used.add(child)
                        queue.append((child, answer+1))

n = int(raw_input())
a = map(int, raw_input().split())
r = [0, 0, 0, 0]

for i in xrange(n): r[a[i] - 1] += 1 << i
print bfs(r)

