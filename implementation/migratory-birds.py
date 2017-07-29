from collections import Counter

n = int(raw_input())
a = map(int, raw_input().split())

value = 0
times = 0
counter = Counter()

for i in xrange(n):
    counter[a[i]] += 1
    if counter[a[i]] > times:
        value = a[i]
        times = counter[a[i]]
        
    if counter[a[i]] == times and value > a[i]:
        value = a[i]
        
print value
        
