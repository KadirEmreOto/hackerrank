
N, M = map(int, raw_input().split())
array = map(int, raw_input().split())

answer = 0
for i in xrange(N):
    for j in xrange(i+1, N):
        if not (array[i] + array[j]) % M:
            answer += 1
print answer

