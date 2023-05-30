#  Напишите функцию для транспонирования матрицы

def transposition(matrix):
    res_out=[]
    n=len(matrix)
    m=len(matrix[0])
    for i in range(m):
        temp=[]
        for j in range(n):
            temp=temp+[matrix[j][i]]
        res_out=res_out+[temp]
    return res_out

matrix = [[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5],[1,2,3,4,5], [1,2,3,4,5],[1,2,3,4,5], [1,2,3,4,5]]
for line in matrix:
    print (*line)
print ()
transposition(matrix)
[[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5],[1,2,3,4,5], [1,2,3,4,5],[1,2,3,4,5], [1,2,3,4,5]]
for line in transposition(matrix):
    print(*line)