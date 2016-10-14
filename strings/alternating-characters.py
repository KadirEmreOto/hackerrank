# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(raw_input())

for t0 in xrange(T):
    text = raw_input()
    
    answer = 0
    current = text[0]
    
    for i in text[1:]:
        if i == current:
            answer += 1
        else:
            current = i
    print answer
