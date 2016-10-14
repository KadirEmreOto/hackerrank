# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(raw_input())

for t0 in xrange(T):
    text = raw_input()
    
    answer = 0
    for i in xrange(len(text) / 2):
        answer += abs(ord(text[i]) - ord(text[-i-1]))
    print answer
