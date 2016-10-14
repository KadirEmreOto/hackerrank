# Enter your code here. Read input from STDIN. Print output to STDOUT

times = [0] * 10**6

N = int(raw_input())
arr = map(int, raw_input().split())

for i in arr:
    times[i] += 1
    
c = 0
for i in xrange(10**6):
    if c == N: break
    if times[i]:
        for j in xrange(times[i]):
            print i,
        c += times[i]
