# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(raw_input())
a = map(int, raw_input().split())
c = Counter(a)

print n - max(c.values())
