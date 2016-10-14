# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = map(int, raw_input().split())
arr = map(int, raw_input().split())
arr.sort()

res = [1] + [0] * N

for c in arr:
    for i in range(c, N+1):
        res[i]+=res[i-c]

print res[N]
