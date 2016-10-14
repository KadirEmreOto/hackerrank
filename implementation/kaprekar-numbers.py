# Enter your code here. Read input from STDIN. Print output to STDOUT

s = int(raw_input())
e = int(raw_input())
check = False
for i in xrange(s, e+1):
    sq = str(i ** 2)
    if sq == "1": print 1,; check = True ; continue
    if len(sq) == 1: continue
    if len(sq) % 2: index = (len(sq) + 1) / 2
    else: index = len(sq) / 2

    try:
        if int(sq[:index]) + int(sq[index:]) == i and int(sq[index:]):
            print i,
            check = True
        
        elif int(sq[:index-1]) + int(sq[index-1:]) == i and int(sq[index-1:]) and len(sq) % 2:
            print i,
            check = True
    except:
        pass
if not check:
    print 'INVALID RANGE'
        
