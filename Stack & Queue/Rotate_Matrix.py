matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

print(matrix)
n=len(matrix)

for i in range(0,n):
    for j in range(i,n):
        temp=matrix[i][j]
        matrix[i][j]=matrix[j][i]
        matrix[j][i]=temp
        
print(matrix)

for i in range(0,n):
    for j in range(0,n//2):
        temp=matrix[i][j]
        matrix[i][j]=matrix[i][n-1-j]
        matrix[i][n-1-j]=temp
    
print(matrix)
    