#-*- coding: UTF-8 -*-
def Seq(array, req):
    dn = [{} for i in xrange(1+req)]
    dn[0] = {0:1}

    array.sort()

    for item in array:
        for i in xrange(req, -1, -1):
            if dn[i] and i+item <= req:
                for c in dn[i]:
                    if c + 1 not in dn[i+item]: dn[i+item][c+1] = 0
                    dn[i+item][c+1] += dn[i][c]

    return dn[-1]

m, r, s = map(int, raw_input().split())
array = map(int, raw_input().split())
array.sort()

a = (r + s) / 2
b = r - a

if r <= s:
    print 0

else:
    n1 = Seq(array, a)
    n2 = Seq(array, b)

    answer = 0
    for i in n1:
        if i in n2:
            answer += n1[i] * n2[i]

    print answer % 1000000007

