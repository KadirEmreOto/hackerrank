
line = raw_input()
answ = 0

for i in xrange(len(line)):
    if i % 3 == 1 and line[i] != 'O': answ += 1
    elif i % 3 != 1 and line[i] != 'S': answ += 1

print answ
        
