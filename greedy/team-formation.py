
import heapq

T = int(raw_input())
for t in xrange(1, T+1):
    line = map(int, raw_input().split())

    N = line[0]; arr = sorted(line[1:])
    if not N: print 0; continue

    result = {arr[0]: [1]}

    for i in arr[1:]:
        if i not in result: result[i] = []
        if (i-1) in result and result[i-1]:
            m = heapq.heappop(result[i-1])
            heapq.heappush(result[i], m+1)
        else:heapq.heappush(result[i], 1)

    answer = 10**5
    for i in result:
        arr = result[i]
        if arr:
            answer = min(answer, heapq.heappop(arr))

    print answer

