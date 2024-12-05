list = open("data.txt",'r')
matrix = []
#Building a matrix out of the file

def isSomething(matrix,i,j,n,m) :
    sum = 0
    if matrix[i][j] == 'X' : 
        match_horizontal_1, match_vertical_1,  match_horizontal_2, match_vertical_2, match_diagonal_1,match_diagonal_2, match_diagonal_3, match_diagonal_4 = '','', '', '', '', '', '',''
        for k in range(1,4) : 
            if  i<n-3 :
                match_vertical_1 += matrix[i+k][j]
            if j<m-3:
                match_horizontal_1 += matrix[i][j+k]
            if i>=3:
                match_vertical_2 += matrix[i-k][j]
            if j>=3 :
                match_horizontal_2 += matrix[i][j-k]
            if j<m-3 and i<n-3:
                match_diagonal_1 += matrix[i+k][j+k]
            if j>=3 and i>=3:  
                match_diagonal_2 += matrix[i-k][j-k]
            if i>=3 and j<m-3 :
                match_diagonal_3 += matrix[i-k][j+k]
            if i<n-3 and j>=3 :
                match_diagonal_4 += matrix[i+k][j-k]
        matches = [match_horizontal_1, match_vertical_1,match_horizontal_2, match_vertical_2, match_diagonal_1, match_diagonal_2, match_diagonal_3, match_diagonal_4]
        sum += matches.count('MAS')
    return sum

for line in list :
    line = line.strip()
    n = len(line)
    matrix_line=[]
    for element in line:
        matrix_line.append(element)
    matrix.append(matrix_line)
    
n = len(matrix) #nombre de lignes
m = len(matrix[0])  #nombre de colonnes 
sum = 0 
for i in range(n):
    for j in range(m):
        sum+= isSomething(matrix,i,j,n,m)
    
print(sum)