# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())

ans = [0] * 100

for _ in xrange(N):
    wd = raw_input().split()
    nb = int(wd[0])
    for i in xrange(nb, 100):
        ans[i] += 1
        
print ' '.join(map(str, ans))
    

    
    
