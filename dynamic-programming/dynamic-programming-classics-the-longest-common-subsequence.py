from pprint import pprint

def LCS(array1, array2):
    matrix = [ [0]*(len(array1)+1) for _ in xrange(len(array2)+1) ]

    for i in xrange(len(array1)):
        x = array1[i]

        for j in xrange(len(array2)):
            y = array2[j]

            if x == y:
                matrix[j+1][i+1] = matrix[j][i] + 1
            else:
                matrix[j+1][i+1] = max(matrix[j][i+1], matrix[j+1][i])


    answer = []
    last_point = (len(matrix)-1, len(matrix[0])-1)

    def SolveMatrix(start=last_point):
        if start[0] == 0 or start[1] == 1: 
            if matrix[start[0]][start[1]] == 1:
                answer.append(array1[0])
            answer.reverse()
            return answer

        top = matrix[start[0]-1][start[1]] 
        lft = matrix[start[0]][start[1]-1]
        current = matrix[start[0]][start[1]] 

        if max(top, lft) == current:
            if top < lft:
                SolveMatrix((start[0], start[1]-1))
            else:
                SolveMatrix((start[0]-1, start[1]))
        else:
            answer.append(array1[start[1]-1])
            SolveMatrix((start[0]-1, start[1]-1))

    SolveMatrix()
    return answer


if __name__ == '__main__':
    n, m = map(int, raw_input().split())
    arr1 = map(str, raw_input().split())
    arr2 = map(str, raw_input().split())

    print ' '.join(LCS(arr1, arr2))
            
