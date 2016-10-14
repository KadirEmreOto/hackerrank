Q = int(raw_input())

for q in xrange(Q):
    K = int(raw_input())
    A = bin(int(raw_input(), 16))[2:]
    B = bin(int(raw_input(), 16))[2:]
    C = bin(int(raw_input(), 16))[2:]

    l = max(len(A), len(B), len(C))

    A = bytearray(A.zfill(l))   # ord('0') = 48
    B = bytearray(B.zfill(l))   # ord('1') = 49
    C = bytearray(C.zfill(l))

    extra = []
    for i in xrange(len(A)):
        if not K: break

        if C[i] == 49 and A[i] == 48 and B[i] == 48:
            B[i] = 49
            K -= 1

        elif C[i] == 48:
            if A[i] == 49 and K > 0: A[i] = 48; K -= 1
            if B[i] == 49 and K > 0: B[i] = 48; K -= 1

        elif C[i] == 49 and A[i] == 49 and B[i] == 49:
            extra.append((i, 1))

        elif C[i] == 49 and A[i] == 49 and B[i] == 48:
            extra.append((i, 2))

    for i, c in extra:
        if not K > 0: break

        if c == 1:
            A[i] = 48
            K -= 1

        elif K > 1 and c == 2:
            A[i] = 48
            B[i] = 49
            K -= 2

    A = int(str(A), 2)
    B = int(str(B), 2)
    C = int(str(C), 2)

    if A | B == C:
        print hex(A)[2:].upper().rstrip('L')
        print hex(B)[2:].upper().rstrip('L')

    else:
        print -1

