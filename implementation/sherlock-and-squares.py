

if __name__ == '__main__':
    T = int(raw_input())

    for t0 in xrange(T):
        a, b = map(int, raw_input().split())
        if int(a ** 0.5) == a ** 0.5:
            print int(b ** 0.5) - int(a ** 0.5) + 1
        else:
            print int(b ** 0.5) - int(a ** 0.5) 


