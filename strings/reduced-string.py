# Enter your code here. Read input from STDIN. Print output to STDOUT

def Solve(string):
    
    swap = True
    while swap:
        swap = False
        
        for i in xrange(len(string)-1):
            if string[i] == string[i+1]:
                string = string[:i] + string[i+2:]
                swap = True
                break
    return string
    

line = raw_input()
a = Solve(line)
if not a:
    a = 'Empty String'
print a
