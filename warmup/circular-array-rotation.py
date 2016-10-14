# Enter your code here. Read input from STDIN. Print output to STDOUT

N, K, Q = map(int, raw_input().split())
arr = map(int, raw_input().split())

K %= N
for _ in xrange(Q):
    q = int(raw_input())
    print arr[q - K]
