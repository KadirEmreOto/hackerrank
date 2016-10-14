
grundy = [0, 0, 1, 1, 2, 2, 3, 3, 4]

T = int(raw_input())
for t in xrange(1, T+1):
    N = int(raw_input())
    array = map(int, raw_input().split())

    answer = 0

    for i in array:
        answer ^= grundy[i % 9]

    if answer > 0:
        print 'Manasa'
    else:
        print 'Sandy'

