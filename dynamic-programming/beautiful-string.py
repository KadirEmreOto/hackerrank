
S = raw_input()
A = []

pre = ''
for i in xrange(len(S)):
    if S[i] != pre: A.append(1)
    else: A[-1] += 1
    pre = S[i]

ans = 0
rel = 0
for i in xrange(len(A)):
    ans += len(A) - i - 1
    if A[i] > 1:
        ans += 1

    if S[rel-2:rel] == S[rel:rel+2]:
        ans -= 1


    if 1 < rel < len(S)-1 and S[rel - 1] == S[rel + 1]:
        ans -= 1

    if rel > 3 and S[rel-3] == S[rel - 1] and S[rel - 2] == S[rel]:
        ans += 1

    rel += A[i]

print ans

