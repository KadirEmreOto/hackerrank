from collections import Counter
n = int(raw_input())
a = Counter(map(int, raw_input().split()))
print a.most_common(1)[0][1]

