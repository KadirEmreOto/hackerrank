
T = int(raw_input())

for t in xrange(T):
    N, K = map(int, raw_input().split())
    array = map(int, raw_input().split())

    answer = 0
    for i in array:
        answer ^= i
    if answer: 
        print 'First'
    else:
        print 'Second'
    
    
