
from bisect import bisect

def lower_bound(array, x):
    index = bisect(array, x)
    if index == len(array) and  array[index-1] != x: return -1
    if array[index-1] == x: return x
    else: return array[index]

def add(node, bit, i):
    node[2].append(i)
    if bit == -1: return

    if binary[bit] == '1' and not node[1]:
        node[1] = [None, None, []]

    if binary[bit] == '0' and not node[0]:
        node[0] = [None, None, []]

    if binary[bit] == '1': add(node[1], bit-1, i)
    else: add(node[0], bit-1, i)

def find(node, bit):
    if bit == -1: return 0

    if binary[bit] == '0':
        if node[1] and l <= lower_bound(node[1][2], l) <= r:
            return (1 << bit) + find(node[1], bit-1)
        return find(node[0], bit-1)

    else:
        if node[0] and l <= lower_bound(node[0][2], l) <= r:
            return (1 << bit) + find(node[0], bit-1)
        return find(node[1], bit-1)

def Binary(number):
    b = bin(number)[:1:-1]
    return (b + '0' * (16 - len(b)))

T = int(raw_input())

for _ in xrange(T):
    N, Q = map(int, raw_input().split())
    arr = map(int, raw_input().split())

    root = [None, None, []]

    for i in xrange(1, N+1):
        binary = Binary(arr[i-1])
        add(root, 15, i)

    if len(arr) > N:
        q, l, r = arr[-3:]
        binary = Binary(q)
        print find(root, 15)

        Q -= 1

    for i in xrange(Q):
        q, l, r = map(int, raw_input().split())
        binary = Binary(q)

        print find(root, 15)

