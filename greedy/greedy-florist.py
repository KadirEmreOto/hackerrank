

N, K = map(int, raw_input().split())
c = map(int, raw_input().split())
c.sort()

answer = sum(c[N-K:N])

i = 0
m = 1

while i < N-K:
    if not i % K: m += 1
    answer += c[N-K-i-1] * m

    i += 1
print answer
