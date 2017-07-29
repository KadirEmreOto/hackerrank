
def valid(number, start, i=0):
    if number == '' and i > 0: return True

    if number.startswith(start):
        return valid(number[len(str(start)):], str(int(start)+1), i+1)
    return False

n = int(raw_input())
for _ in xrange(n):
    a = raw_input()

    found = False
    for i in xrange(1, len(a)-1):
        if valid(a, a[:i]):
            print 'YES', a[:i]
            found = True
            break

    if not found:
        print 'NO'


