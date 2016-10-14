num2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

def number(Number):
    if 1 <= Number <= 19:
        return num2words1[Number].lower().strip()
    elif 20 <= Number <= 99:
        tens, below_ten = divmod(Number, 10)
        if not below_ten: return num2words2[tens - 2].lower().strip()
        return num2words2[tens - 2].lower().strip() + ' ' + num2words1[below_ten].lower().strip()
    else:
        print("Number out of range")

def Write(h, m):
    if m == 0:
        print "{} o' clock".format(number(h))

    elif 0 < m < 30 and m != 15:
        if m == 1:
            print "{} minute past {}".format(number(m), number(h))
        else:
            print "{} minutes past {}".format(number(m), number(h))
        
    elif m == 15:
        print "quarter past {}".format(number(h))

    elif m == 30:
        print "half past {}".format(number(h))

    elif 30 < m < 60 and m != 45:
        if 60-m == 1:
            print "{} minute to {}".format(number(60-m), number(h+1))
        else:
            print "{} minutes to {}".format(number(60-m), number(h+1))

    elif m == 45:
        print "quarter to {}".format(number(h+1))

h = int(raw_input().strip())
m = int(raw_input().strip())

Write(h,m)
