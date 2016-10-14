# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(raw_input())

for _ in xrange(T):
    print int('1'*32, 2) - int(raw_input())    
