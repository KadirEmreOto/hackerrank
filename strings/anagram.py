# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

T = int(raw_input())

for t0 in xrange(T):
    string = raw_input()
    
    if len(string) % 2:
        print '-1'
        continue
        
    S1 = string[:len(string)/2]
    S2 = string[len(string)/2:]
    
    C1 = Counter(S1)
    C2 = Counter(S2)
    
    answer = 0
    for i in C1:
        if i not in C2:
            answer += C1[i]
        elif C1[i] > C2[i]: 
            answer += C1[i] - C2[i]
            
    print answer
            
