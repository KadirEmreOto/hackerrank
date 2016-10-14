
s = raw_input().strip()
s = s.replace(' ', '')

r = int(len(s) ** 0.5)
c = r
while c*r < len(s): 
    if r < c:
        r += 1
    else:
        c += 1

for i in range(c):
    temp = ''
    for j in range(r):
        if i+j*c < len(s):
            temp += s[i+j*c]
    print temp,
