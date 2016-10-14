# Enter your code here. Read input from STDIN. Print output to STDOUT

V = int(raw_input().strip())
n = int(raw_input().strip())
l = map(int, raw_input().strip().split())

print l.index(V)
