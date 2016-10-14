
def ZAlgorithm(text):
    L = len(text)
    Z = [0] * L

    pos = 1
    cnt = 0

    while pos < L:
        if pos + cnt < L and text[pos + cnt] == text[cnt]:
            cnt += 1

        else:

            if not cnt:
                pos += 1
                continue

            Z[pos] = cnt
            flag = cnt
            i = 1

            while i < cnt:
                if text[pos + i] == text[0]:
                    if Z[i] != cnt - i:
                        Z[pos + i] = min(cnt - i, Z[i])

                    else:
                        flag = i
                        break
                i += 1

            pos += flag
            cnt -= flag
    return Z

for i in xrange(input()):
    s = raw_input()
    z = ZAlgorithm(s)
    print sum(z) + len(s)

