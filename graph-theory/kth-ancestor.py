#-*- coding: UTF-8 -*-
import math
def Build(x, y):
    dn[x][0] = y

    index = 1
    while y != 0:
        try:
            dn[x][index] = dn[y][index-1]
            y = dn[y][index-1]
            index += 1
        except:
            print x, y, index
            quit()

def Find(node, k):
    mp = int(math.log(k, 2))

    if 2 ** mp == k:
        return dn[node][mp]

    else:
        return Find(dn[node][mp], k - 2 ** mp)

T = int(raw_input())

for _ in xrange(T):
    P = int(raw_input())
    dn = {} 

    for _ in xrange(P):
        x, y = map(int, raw_input().split())

        if x not in dn: dn[x] = [0] * 18
        if y not in dn: dn[y] = [0] * 18
        #print x, y
        
        Build(x, y)

    Q = int(raw_input())

    for _ in xrange(Q):
        q = map(int, raw_input().split())
        
        if q[0] == 0: # Add Leaf
            y, x = q[1:]
            if x not in dn: dn[x] = [0] * 18
            if y not in dn: dn[y] = [0] * 18
            
            Build(x, y)

        elif q[0] == 1: # Delete Leaf
            dn[q[1]] = [0]*18

        else: 
            x, y = q[1:]
            if x not in dn:
                print 0
            else:
                print Find(x, y)
