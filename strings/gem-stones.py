# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())

arr = []
for n0 in xrange(N):
    text = raw_input()
    arr.append(text)

answer = 0
for i in set(arr[0]):
    check = True
    for t in arr[:]:
        if i not in t:
            check = False
            break
    if check:
        answer += 1
        
print answer
