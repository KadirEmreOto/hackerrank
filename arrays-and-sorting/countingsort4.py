
N = int(raw_input())

arr = []
for i in xrange(N / 2):
    num = int(raw_input().split()[0])
    arr.append((num, '-'))

for i in xrange(N / 2):
    line = raw_input().split()
    
    num = int(line[0])
    wor = line[1]
    
    arr.append((num, wor))

arr.sort(key=lambda x: x[0])
for i in arr:
    print i[1], 

