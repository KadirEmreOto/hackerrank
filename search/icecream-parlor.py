# Enter your code here. Read input from STDIN. Print output to STDOUT

def Search():
    for index in xrange(N - 1):
        first = array[index]
        if first > cost: continue
        
        for s in xrange(index+1, N):
            second = array[s]
            
            if first + second == cost:
                return index + 1, s + 1



if __name__ == '__main__':
    T = int(raw_input())

    for t0 in xrange(T):
        cost = int(raw_input())
        N = int(raw_input())
        array = map(int, raw_input().split())

        answer = Search()
        print answer[0], answer[1]

