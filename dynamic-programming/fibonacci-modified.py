# Enter your code here. Read input from STDIN. Print output to STDOUT


def T(n, a, b):
    if n == 1: return a
    if n == 2: return b
    return T(n-1, a, b)**2 + T(n-2, a, b)

a, b, n = raw_input().strip().split()
print T(int(n), int(a), int(b))
    
