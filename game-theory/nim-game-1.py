# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(raw_input())

for t in xrange(T):
    N = int(raw_input())
    
    array = map(int, raw_input().split())
    answer = 0
    for i in array:
        answer ^= i
        
    if not answer:
        print 'Second'
    else:
        print 'First'
