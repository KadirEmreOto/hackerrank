# Enter your code here. Read input from STDIN. Print output to STDOUT
import string

text = raw_input().lower()

check = True
for i in string.ascii_lowercase:
    if i not in text:
        check = False
        break
        
if check:
    print "pangram"
else:
    print "not pangram"
 
