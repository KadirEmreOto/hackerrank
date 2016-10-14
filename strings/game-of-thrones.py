from collections import Counter

string = raw_input()
counter = Counter(string)
 
found = True
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
odd = 0
for i in counter:
    if counter[i] % 2:
        odd += 1
    if odd > 1:
        found = False
        break

if not found:
    print("NO")
else:
    print("YES")

