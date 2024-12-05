def look(i,j,mat,wish):
    if len(wish)==0:
        return True
    if i<0 or i>=len(mat):
        return False
    if j<0 or j>=len(mat[i]):
        return False
    if mat[i][j]!=wish[0]:
        return False
    return True

def diag(i,j,a,b,mat):
    return look(i+a[0], j+a[1], mat, "M") and look(i+b[0], j+b[1], mat, "S")

def test(i,j,mat):
    if (diag(i,j,(-1,-1),(+1,+1), mat) or diag(i,j,(+1,+1),(-1,-1),mat)) and (diag(i,j,(-1,+1), (+1,-1), mat) or diag(i,j, (+1,-1), (-1,+1),mat)):
        return 1
    return 0

list = open("data.txt",'r')

mat = [l.strip() for l in list]
count = 0
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j]=='A':
            count+=test(i,j,mat)
print(count)