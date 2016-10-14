import time

T = int(raw_input())

s = time.clock()
for t0 in xrange(T):
    N = int(raw_input())
    array = map(int, raw_input().split())

    max_ = 0
    answer = 0
    
    for i in xrange(len(array)):
        item = array[-i-1]
        max_ = max(max_, item)
        if max_ - item > 0:
            answer += max_ - item
    print answer
