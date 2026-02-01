# matrix_1 = [ [1, 2, 3],
#              [4, 5, 6],
#              [7, 8, 9] ]


# 'U': [['U1', 'U2', 'U3'], ['U4', 'U5', 'U6'], ['U7', 'U8', 'U9']],
# 'R': [['R1', 'R2', 'R3'], ['R4', 'R5', 'R6'], ['R7', 'R8', 'R9']],
# 'F': [['F1', 'F2', 'F3'], ['F4', 'F5', 'F6'], ['F7', 'F8', 'F9']],
# 'D': [['D1', 'D2', 'D3'], ['D4', 'D5', 'D6'], ['D7', 'D8', 'D9']],
# 'L': [['L1', 'L2', 'L3'], ['L4', 'L5', 'L6'], ['L7', 'L8', 'L9']],
# 'B': [['B1', 'B2', 'B3'], ['B4', 'B5', 'B6'], ['B7', 'B8', 'B9']]

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

# test_current_State = "[['G', 'B', 'B'], ['G', 'W', 'B'], ['G', 'G', 'B']][['Y', 'Y', 'Y'], ['O', 'B', 'R'], ['W', 'W', 'W']][['O', 'R', 'R'], ['W', 'R', 'W'], ['O', 'R', 'R']][['G', 'B', 'B'], ['G', 'Y', 'B'], ['G', 'G', 'B']][['W', 'W', 'W'], ['O', 'G', 'R'], ['Y', 'Y', 'Y']][['O', 'O', 'R'], ['Y', 'O', 'Y'], ['O', 'O', 'R']]"

# print(test_current_State)

# test_current_State = test_current_State.replace("'", "").replace(" ", "").replace("[", "").replace("]", "").replace(",","")

# print(test_current_State)

# test_current_State = test_current_State.replace("W", "U").replace("Y", "D").replace("R", "F").replace("O", "B").replace("G", "L").replace("B", "R")

# print(test_current_State)


# # String de generat {'F': [['F1', 'F2', 'F3'], ['F4', 'F5', 'F6'], ['7F', 'F8', 'F9']],

# F = [[],[],[]]
# for i in range(1, 10):
#    if i < 4:
#         F[0].append("F" + str(i))
#    elif i < 7:
#         F[1].append("F" + str(i))
#    else:
#         F[2].append("F" + str(i))

        

# print(F)
    


class TestCubRubik:
    def __init__(self):
        self.cube = self.gen_cube()

    def gen_cube(self):  
        # Genereaza un cub Rubik 3x3x3 cu fete numerotate
        cube_faces = ['U', 'D', 'F', 'B', 'L', 'R']
        return { face: [[face for i in range(3)] for j in range(3)] for face in cube_faces }
    
    def get_cube_from_user_Input(self, user_in):
        print("nonthing for now")

     
#test_cube = TestCubRubik()
#print(test_cube.cube)

color_solving = False

user_option = input("Do you want to input custom colors for the cube? (yes/no): ").strip().lower()
if user_option == 'yes':
    color_solving = True
    from user_colorPicker import ask_user_for_colors