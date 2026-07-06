matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# print(matrix)

# for num in matrix:
#     print(num)

# for row in matrix:
#     for val in row:
#         print(val,end =" ")
#     print()    

# row = len(matrix)
# col = len(matrix[0])

# for i in range(row):
#     for j in range(col):
#         print(matrix[i][j],end = " ")

rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")