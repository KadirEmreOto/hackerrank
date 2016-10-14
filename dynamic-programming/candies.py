

N = int(raw_input())

answer = 0
arr = [0]*N
fromLeft = [1]*N
fromRight = [1]*N
for i in xrange(N):
    arr[i] = int(raw_input())

for i in xrange(N-1):
    if arr[N-i-1] < arr[N-i-2]:
        fromRight[N-i-2] = fromRight[N-i-1] + 1
    else:
        fromRight[N-i-2] = 1
    
    if arr[i] < arr[i+1]:
        fromLeft[i+1] = fromLeft[i] + 1
    else:
        fromLeft[i+1] = 1
for i in range(N):
    answer += max(fromLeft[i],fromRight[i])
print answer

