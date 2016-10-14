import sys

def BubbleSort(array):
    answer = 0
    swaped = False

    for i, v in enumerate(array):
        if (v - 1) - i > 2:
            return "Too chaotic"

    for i in xrange(0, len(array) - 1):
        for j in xrange(0, len(array) - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                answer += 1
                swaped = True

        if swaped: swaped = False
        else: break
    return answer


T = int(raw_input())
for t in xrange(T):
    N = int(raw_input().strip())
    A = map(int, raw_input().split())
    print BubbleSort(A)

