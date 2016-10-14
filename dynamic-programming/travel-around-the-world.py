from random import randrange

def check(node):
    answer = True
    current = 0
    for i in xrange(N):
        index = (node+i) % N
        current = min(C, current+fuel[index])
        current -= cost[index]
        if current < 0:
            answer = False
            break
    return answer

N, C = map(int, raw_input().split())
fuel = map(int, raw_input().split())
cost = map(int, raw_input().split())

fail = 0
node = randrange(0, N)

while not check(node):
    fail += 1
    node = randrange(0, N)
    if fail == 1000:
        print 0
        quit()

answer = 1
lack = 0
for i in xrange(1, N):
    index = (node-i) % N
    lack = cost[index] - fuel[index] + lack
    if lack <= 0:
        lack = 0
        answer += 1

print answer

