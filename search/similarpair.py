import sys, resource, math

sys.setrecursionlimit(100005)
resource.setrlimit(resource.RLIMIT_STACK, (65532000, 65532000))
    
class SegmentTree(object):
    def __init__(self, array):
        self.array = array

        power = int(math.ceil(math.log(len(array), 2)))
        self.tree = [0] * ((2**(power + 1)) - 1)
        self.consructTree()

    def consructTree(self, low=0, high=None, pos=0):
        if high is None: high = len(self.array)-1
        if low == high:
            self.tree[pos] = self.array[low]
            return

        mid = (low + high) // 2
        self.consructTree(low, mid, 2*pos+1)
        self.consructTree(mid+1, high, 2*pos+2)
        self.tree[pos] = self.tree[2*pos+1] + self.tree[2*pos+2]

    def update(self, index, value, pos=0, low=0, high=None):
        if high is None: high = len(self.array)-1

        if low <= index <= high: # total overlap
            if value: self.tree[pos] += 1
            else: self.tree[pos] -= 1

            if low == high: return

            mid = (low + high) // 2
            if index <= mid:
                self.update(index, value, 2*pos+1, low, mid)
            else:
                self.update(index, value, 2*pos+2, mid+1, high)

    def query(self, qlow, qhigh, pos=0, low=0, high=None):
        if high is None: high = len(self.array)-1

        if qlow <= low and high <= qhigh: # total overlap
            return self.tree[pos]

        elif high < qlow or qhigh < low: # no overlap
            return 0

        mid = (low + high) // 2
        return self.query(qlow, qhigh, 2*pos+1, low, mid) + \
                self.query(qlow, qhigh, 2*pos+2, mid+1, high)

def DFS(node):
    global answer
    segtree.update(node, 1)

    for it in tree[node]:
        answer += segtree.query(it - T, it + T)
        DFS(it)
    segtree.update(node, 0)


tree = {}
N, T = map(int, raw_input().strip().split())

S = -1

for i in range(N - 1):
    s1, e1 = map(int, raw_input().strip().split())
    if S == -1: S = s1
    
    if not s1 in tree: tree[s1] = []
    if not e1 in tree: tree[e1] = []
    tree[s1].append(e1)

visited = [0] * (N+1)
segtree = SegmentTree(visited)
answer = 0
DFS(S)
print answer
