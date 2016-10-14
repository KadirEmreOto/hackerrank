
N = int(raw_input())
arr = map(int, raw_input().split())
arr.sort()

cost = -1
answer = []
for i in xrange(N-1):
    if arr[i+1] - arr[i] < cost or cost == -1:
        cost = arr[i+1] - arr[i]
        answer = [(arr[i], arr[i+1])]

    elif (arr[i+1] - arr[i]) == cost:
        answer.append((arr[i], arr[i+1]))

for i in answer:
    for j in i:
        print j, 

