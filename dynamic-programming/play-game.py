# Enter your code here. Read input from STDIN. Print output to STDOUT


def Solve():
    index = 3 
    
    while index < N:
        a = s[index] - M[index-3]
        b = s[index] - M[index-2]
        c = s[index] - M[index-1]
        M[index] = max(a,b,c)
        index+=1
    
T = int(raw_input())

for t0 in xrange(T):
    N = int(raw_input())
    arr = map(int, raw_input().split())
    arr.reverse()
    
    s = [arr[0]]
    for i in arr[1:]:
        s.append(s[-1] + i)
    M = s[:3] + [-1] * (N-3)

    Solve()
    print M[-1]
    
    
