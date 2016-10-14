# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
arr = map(int, raw_input().split())
arr.sort()
print arr[N / 2]
