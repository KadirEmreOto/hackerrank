
N = int(raw_input())
array = raw_input()

i = 0
answer = 0
while i + 2 < N:
    if array[i] == '0' and array[i+1] == '1' and array[i+2] == '0':
        answer += 1
        i += 2
    i += 1
print answer

