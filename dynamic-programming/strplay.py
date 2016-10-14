
# Longest Palindromic Subsequence
def LPS(string):
    lenght = len(string)
    matrix = [[0]*lenght for i in xrange(lenght)]

    for l in xrange(0, lenght+1):
        for i in xrange(0, lenght-l):
            if string[i] == string[i+l]:
                if l == 0:
                    matrix[i][i+l] = 1
                elif l == 1:
                    matrix[i][i+l] = 2
                else:
                    matrix[i][i+l] = 2 + matrix[i+1][i+l-1]

            else:
                matrix[i][i+l] = max(matrix[i][i+l-1], matrix[i+1][i+l])

    return matrix

if __name__ == '__main__':
    string = raw_input()
    lenght = len(string)
    
    matrix = LPS(string)
    answer = 0
    for i in xrange(1, lenght-1):
        t = matrix[0][i] * matrix[i+1][lenght-1]
        if t > answer:
            answer = t

    print answer

