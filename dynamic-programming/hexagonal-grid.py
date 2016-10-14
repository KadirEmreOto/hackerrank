
T = int(raw_input())

for t in xrange(T):
    N = int(raw_input())
    top = list(raw_input())
    bottom = list(raw_input())

    for i in xrange(N):

        if top[i] == '0':
            if bottom[i] == '0':
                top[i] = '1'
                bottom[i] = '1'

            elif i != N-1 and top[i+1] == '0':
                top[i] = top[i+1] = '1'

        if bottom[i] == '0':
            if i != N-1 and top[i+1] == '0':
                bottom[i] = '1'
                top[i+1] = '1'

            elif i != N-1 and bottom[i+1] == '0':
                bottom[i] = bottom[i+1] = '1'

    if '0' in top or '0' in bottom:
        print 'NO'
    else:
        print 'YES'

