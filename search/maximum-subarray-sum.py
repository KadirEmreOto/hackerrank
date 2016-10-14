
from bisect import bisect

def lower_bound(array, x):
    index = bisect(array, x)
    if index >= len(array): return 0, index
    else: return array[index], index

T = int(raw_input().strip())

for t0 in xrange(T):
    N, M = map(int, raw_input().strip().split())
    array = map(int, raw_input().strip().split())

    sumarray = [0]
    for index in xrange(N):
        item = array[index]
        sumarray.append((sumarray[-1] + item) % M )


    result = max(sumarray)
    ordered = []
    for item in sumarray[1:]:
        lower, index = lower_bound(ordered, item)
        ordered.insert(index, item)


        if lower and (item - lower + M) > result:
            result = (item - lower + M)

    print result

