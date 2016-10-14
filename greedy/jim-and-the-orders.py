# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())

array = []

for i in xrange(N):
    t, d = map(int, raw_input().split())
    array.append((i, t+d, d))

sorted_ = sorted(array, key=lambda k: (k[1], k[0]))

for i in sorted_:
    print i[0] + 1 ,
    
