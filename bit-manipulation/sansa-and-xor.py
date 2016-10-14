
T = int(raw_input())

for _ in xrange(T):
    N = int(raw_input())
    arr = map(int, raw_input().split())
    ans = 0

    for i in xrange(N):
        if (i+1)*(N-i) % 2:
            ans ^= arr[i]
    print ans
