# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for t in xrange(1, T+1):
    N = int(raw_input())
    A = []
    B = []

    for i in xrange(N): A.append(int(raw_input()))
    for i in xrange(N): B.append(int(raw_input()))

    answer = 0
    for i in xrange(N): answer ^= (abs(A[i] - B[i]) - 1)

    if answer: print 'player-2'
    else: print 'player-1'
