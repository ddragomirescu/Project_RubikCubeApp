# matrix_1 = [ [1, 2, 3],
#              [4, 5, 6],
#              [7, 8, 9] ]

# print("Original Matrix:", matrix_1)
# #matrix[::-1] # This will reverse the rows of the matrix

# print("Reversed Matrix:", matrix_1[::-1])

# print("Reversed Rows Matrix:", [row[::-1] for row in matrix_1])

# print(matrix_1[::-1])  # This will reverse the rows and then the columns, resulting in the original matrix

# print([list(row) for row in zip(*matrix_1[::-1])]) 

# print([list(row) for row in zip(*matrix_1)][::-1])

# print(matrix_1[0][::-1])  # This will reverse the rows and then the columns, resulting in the original matrix

    # Crearea unei instanțe a cubului Rubik
    # cub = CubRubik.CubRubik()
    
    # Afișarea stării inițiale a cubului
    #cub.display()
    
    # Exemplu de rotație a feței "Sus"
    # cub.rotate("U")
    # cub.rotate("R-")
    # cub.rotate("U")
    # cub.rotate("B")
    # cub.rotate("L")
    # cub.rotate("D-")
    # cub.rotate("F")
    # cub.rotate("L-")
    
    # Afișarea stării cubului după rotație
    #cub.display()
    
    # Exemplu de rotație a feței "Fata" în sens invers acelor de ceasornic
    #cub.rotate("F-")
    
    # Afișarea stării cubului după rotația inversă
    # cub.display()
    
    # print("Fata 'Sus' a cubului Rubik:" + str(cub.cube['U']))
    # print("Fata 'Jos' a cubului Rubik:" + str(cub.cube['D']))
    # print("Fata 'Fata' a cubului Rubik:" + str(cub.cube['F']))

test_current_State = "[['G', 'B', 'B'], ['G', 'W', 'B'], ['G', 'G', 'B']][['Y', 'Y', 'Y'], ['O', 'B', 'R'], ['W', 'W', 'W']][['O', 'R', 'R'], ['W', 'R', 'W'], ['O', 'R', 'R']][['G', 'B', 'B'], ['G', 'Y', 'B'], ['G', 'G', 'B']][['W', 'W', 'W'], ['O', 'G', 'R'], ['Y', 'Y', 'Y']][['O', 'O', 'R'], ['Y', 'O', 'Y'], ['O', 'O', 'R']]"

print(test_current_State)

test_current_State = test_current_State.replace("'", "").replace(" ", "").replace("[", "").replace("]", "").replace(",","")

print(test_current_State)

test_current_State = test_current_State.replace("W", "U").replace("Y", "D").replace("R", "F").replace("O", "B").replace("G", "L").replace("B", "R")

print(test_current_State)