
T = int(raw_input())

for _ in xrange(T):
    string = raw_input()

    answer = -1
    for i in xrange(len(string)/2):
        if string[i] != string[-i-1]:
            straigt = string[i:len(string)-i-1]
            reverse = straigt[::-1]
            if straigt == reverse:
                answer = len(string) - i - 1
            else:
                answer = i
            break
    print answer
