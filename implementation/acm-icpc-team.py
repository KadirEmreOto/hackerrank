
from itertools import combinations

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0

for topic_i in xrange(n):
    topic_t = str(raw_input().strip())
    topic.append(topic_t)

def Check(a,b):
    count = 0
    for i in range(len(a)):
        if a[i] == '1' or b[i] == '1':
            count += 1
    return count

maximum_topic = 0
count = 0
for p2 in combinations(topic, 2):
    top = Check(p2[0], p2[1])

    if maximum_topic == top:
        count += 1

    if maximum_topic < top:
        maximum_topic = top
        count = 1
        
print maximum_topic
print count
    

