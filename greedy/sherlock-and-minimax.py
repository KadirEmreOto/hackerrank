from bisect import bisect, bisect_left

N = int(raw_input())
array = sorted(map(int, raw_input().split()))
P , Q = map(int, raw_input().split())
S , E = bisect(array, P), bisect(array, Q)

if P > Q:
    P, Q = Q, P

if S == 0:
    answer = array[0] - P
    M = P

else:
    if (array[S] + array[S-1]) / 2 >= P:
        answer = (array[S] - array[S-1]) / 2
        M = (array[S] + array[S-1]) / 2
    else:
        answer = array[S] - P
        M = P

if E > N-1:
    if answer < Q - array[-1]:
        answer = Q - array[-1]
        M = Q

    elif answer == Q - array[-1] and M > Q:  
        M = Q

else:
    if (array[E] + array[E-1]) / 2 <= Q:
        if answer == (array[E] - array[E-1]) / 2:
            if M > (array[S] + array[S-1]) / 2:
                M = (array[S] + array[S-1]) / 2

        elif answer < (array[E] - array[E-1]) / 2:
            answer = (array[E] - array[E-1]) / 2
            M = (array[E] + array[E-1]) / 2

    else:
        if answer == Q - array[E-1]:
            if M > Q:
                M = Q

        elif answer < Q - array[E-1]:
            answer = Q - array[E-1]
            M = Q

for i in xrange(S, bisect_left(array, Q)-1):
    if answer == (array[i+1] - array[i])/2:
        if M > (array[i+1] + array[i])/2:
            M = (array[i+1] + array[i])/2

    elif answer < (array[i+1] - array[i])/2:
        answer = (array[i+1] - array[i])/2
        M = (array[i+1] + array[i])/2


print M
