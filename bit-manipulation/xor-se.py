#-*- coding: UTF-8 -*-

def xor(x):
    if x % 4 == 0: return x
    if x % 4 == 1: return 1
    if x % 4 == 2: return x+1
    if x % 4 == 3: return 0

def find(x):
    # 3 + 4t
    for i in xrange(4):
        if ((x+1 - i) % 4) == 3:
            x3 = x+1 - i
            break

    if x3 % 16 == 3: answer = x3
    elif x3 % 16 == 7: answer = 4
    elif x3 % 16 == 11: answer = x3 + 4
    elif x3 % 16 == 15: answer = 0

    # 4t
    x4 = x / 4
    answer ^= xor(x4)<<2

    # 1
    x1 = (((x-1) / 4 + 1) % 2)
    answer ^= x1

    #print 'x:', x, 'x3:', x3,'x4:', x4,'x1:', x1,'Ans:', answer
    return answer

N = int(raw_input())

for i in xrange(N):
    x, y = map(int, raw_input().split())

    print find(y) ^ find(x-1)

