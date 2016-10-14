
N = int(raw_input())
K = int(raw_input())

array = []
for _ in xrange(N):
    array.append(int(raw_input()))

array.sort()

answer = array[K-1] - array[0]
for i in xrange(1, N-K+1):
    answer = min(answer, array[i + K-1] -array[i])

print answer
