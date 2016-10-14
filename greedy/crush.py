
N, M = map(int, raw_input().split())

array = [0]*N
for _ in xrange(M):
    a, b, k = map(int, raw_input().split())
    array[a-1] += k
    if b < N: array[b] -= k

temp = 0
answer = 0

for i in array:
    temp += i
    answer = max(answer, temp)

print answer

