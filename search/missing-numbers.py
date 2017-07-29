# Enter your code here. Read input from STDIN. Print output to STDOUT
from bisect import bisect

n = int(raw_input().strip())
a = map(int, raw_input().strip().split())

m = int(raw_input().strip())
b = map(int, raw_input().strip().split())

counter = {}
for i in b:
    if not i in counter:
        counter[i] = [0, 1]
    else:
        counter[i][1] += 1
        
for i in a:
    counter[i][0] += 1
    
for i in counter:
    if counter[i][0] != counter[i][1]:
        print i,



    

