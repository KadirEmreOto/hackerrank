from collections import defaultdict

n, k = map(int, raw_input().split())

if k == 1: print 1; quit()

array = map(int, raw_input().split())
counter = defaultdict(int)
answer  = 0

for i in array: counter[i % k] += 1
for i in xrange(1, k / 2 + 1):
    if not k % 2 and i == k / 2 and counter[k/2]: answer += 1; continue
    #print i, counter[i], counter[k-i]
    answer += max(counter[i], counter[k-i])

if counter[0]: answer += 1

print answer

