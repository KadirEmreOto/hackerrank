# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(raw_input())


for t0 in xrange(T):
    count = int(raw_input()) - 1
    a = int(raw_input())
    b = int(raw_input())

    times = count + 1

    if a > b: a, b = b,a
    if a == b: times = 1
    
    for c in xrange(times):
        print a*(count-c) + b*c,
    print
    
