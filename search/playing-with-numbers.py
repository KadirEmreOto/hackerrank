#-*- coding: UTF-8 -*-
import sys
from bisect import *

def AbsSum(array):
    result = 0

    for i in array:
        if i < 0:
            result -= i
        else:
            result += i

    return result

inp = sys.stdin.read().split('\n')

N = int(inp[0].strip())
array = map(int, inp[1].strip().split())

Q = int(inp[2].strip())
query = map(int, inp[3].strip().split())

array.sort()
abssum = AbsSum(array)

q = 0
q0L = bisect_left(array, 0) # 4
q0R = bisect(array, 0)      # 5

sumlist = [0]
for i in array:
    sumlist.append(sumlist[-1]+i)

result = ''

for i in xrange(Q):
    q += query[i]
    s = abssum
    if q > 0:
        q1 = bisect(array, -q)
        s -= q1 * q
        s += (N - q0L) * q

        s += q * (q0L-q1) - 2 * (sumlist[q1] - sumlist[q0L])

    else:
        q1 = bisect_left(array, -q)   #[-4, -3, -2, -1,   0,  1,  2,  3, 4]
        s += (N - q1) * q             #[-4, -7, -9, -10,-10, -9, -7, -4, 0] 

        s -= q0R * q
        s += -(q1 - q0R)*q - 2 * (sumlist[q1] - sumlist[q0R])

    result += '{}\n'.format(s)
sys.stdout.write(result)




