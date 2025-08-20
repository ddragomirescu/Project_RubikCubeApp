matrix_1 = [ [1, 2, 3],
             [4, 5, 6],
             [7, 8, 9] ]

print("Original Matrix:", matrix_1)
#matrix[::-1] # This will reverse the rows of the matrix

print("Reversed Matrix:", matrix_1[::-1])

print("Reversed Rows Matrix:", [row[::-1] for row in matrix_1])

print(matrix_1[::-1])  # This will reverse the rows and then the columns, resulting in the original matrix

print([list(row) for row in zip(*matrix_1[::-1])]) 

print([list(row) for row in zip(*matrix_1)][::-1])

print(matrix_1[0][::-1])  # This will reverse the rows and then the columns, resulting in the original matrix

