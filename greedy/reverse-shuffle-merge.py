from collections import defaultdict

string = raw_input()[::-1]
length = len(string) / 2

have = defaultdict(int)
want = defaultdict(int)

for s in string:
    have[s] += 1
    if have[s] & 1: want[s] += 1

answer = bytearray('z'*length)
index = 0

for s in string:
    if not want[s] > 0: continue
    if index >= length: break

    while index > 0 and want[chr(answer[index-1])] < have[chr(answer[index-1])] and answer[index-1] > ord(s):
        want[chr(answer[index-1])] += 1
        index -= 1

    answer[index] = ord(s)
    index += 1
    want[s] -= 1
    have[s] -= 1
print answer

