# Enter your code here. Read input from STDIN. Print output to STDOUT

times = [0] * 100

N = int(raw_input())
arr = map(int, raw_input().split())

for i in arr:
    times[i] += 1
    
print ' '.join(map(str, times))
