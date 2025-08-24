# CubRubik.py
class CubRubik:
    def __init__(self):
        self.cube = self.gen_cube()

    def gen_cube(self):  
        # Genereaza un cub Rubik 3x3x3 cu fete numerotate
        cube_faces = ['U', 'D', 'F', 'B', 'L', 'R']
        return { face: [[face + str(j*3 + i + 1) for i in range(3)] for j in range(3)] for face in cube_faces }
       

    
    def rotate_face(self, face, direction="clockwise"):
        # Rotatie F cubului cu 90 de grade in sensul accelor de ceasornic 
        if direction == "clockwise":
            self.cube[face] = [list(row) for row in zip(*self.cube[face][::-1])]
        elif direction == "counterclockwise":
            # Rotatie F cubului cu 90 de grade in sens trigonometric
            self.cube[face] = [list(row) for row in zip(*self.cube[face])][::-1]

        # Rotirea marginilor adiacente
        if face == 'U':
            f = [self.cube['F'][0][i] for i in range(3)]
            b = [self.cube['B'][0][i] for i in range(3)]
            l = [self.cube['L'][0][i] for i in range(3)]
            r = [self.cube['R'][0][i] for i in range(3)]

            if direction == "clockwise":
                for i in range(3):
                    self.cube['F'][0][i] = r[i]
                    self.cube['B'][0][i] = l[i]
                    self.cube['L'][0][i] = f[i]
                    self.cube['R'][0][i] = b[i]
                    
            elif direction == "counterclockwise":
               for i in range(3):
                    self.cube['F'][0][i] = l[i]
                    self.cube['B'][0][i] = r[i]
                    self.cube['L'][0][i] = b[i]
                    self.cube['R'][0][i] = f[i]

        elif face == 'D':
            f = [self.cube['F'][2][i] for i in range(3)]
            b = [self.cube['B'][2][i] for i in range(3)]
            l = [self.cube['L'][2][i] for i in range(3)]
            r = [self.cube['R'][2][i] for i in range(3)]
            
            if direction == "clockwise":
                for i in range(3):
                    self.cube['F'][2][i] = l[i]
                    self.cube['B'][2][i] = r[i]
                    self.cube['L'][2][i] = b[i]
                    self.cube['R'][2][i] = f[i]

            elif direction == "counterclockwise":
                for i in range(3):
                    self.cube['F'][2][i] = r[i]
                    self.cube['B'][2][i] = l[i]
                    self.cube['L'][2][i] = f[i]
                    self.cube['R'][2][i] = b[i]

        elif face == 'F':
            u = [self.cube['U'][2][i] for i in range(3)]
            d = [self.cube['D'][0][i] for i in range(3)]
            l = [self.cube['L'][i][2] for i in range(3)]
            r = [self.cube['R'][i][0] for i in range(3)]
            
            if direction == "clockwise":
                for i in range(3):
                    self.cube['U'][2][2-i] = l[i]
                    self.cube['D'][0][2-i] = r[i]
                    self.cube['L'][i][2] = d[i]
                    self.cube['R'][i][0] = u[i]

            elif direction == "counterclockwise":
                for i in range(3):
                    self.cube['U'][2][i] = r[i]
                    self.cube['D'][0][i] = l[i]
                    self.cube['L'][2-i][2] = u[i]
                    self.cube['R'][2-i][0] = d[i]

        elif face == 'B':
            u = [self.cube['U'][0][i] for i in range(3)]
            d = [self.cube['D'][2][i] for i in range(3)]
            l = [self.cube['L'][i][0] for i in range(3)]
            r = [self.cube['R'][i][2] for i in range(3)]
            
            if direction == "clockwise":
                for i in range(3):
                    self.cube['U'][0][i] = r[i]
                    self.cube['D'][2][i] = l[i]
                    self.cube['L'][2-i][0] = u[i]
                    self.cube['R'][2-i][2] = d[i]
            
            elif direction == "counterclockwise":
                for i in range(3):
                    self.cube['U'][0][2-i] = l[i]
                    self.cube['D'][2][2-i] = r[i]
                    self.cube['L'][i][0] = d[i]
                    self.cube['R'][i][2] = u[i]

        elif face == 'L':
            u = [self.cube['U'][i][0] for i in range(3)]
            d = [self.cube['D'][i][0] for i in range(3)]
            f = [self.cube['F'][i][0] for i in range(3)]
            b = [self.cube['B'][i][2] for i in range(3)]
            
            if direction == "clockwise":
                for i in range(3):
                    self.cube['U'][i][0] = b[2-i]
                    self.cube['D'][i][0] = f[i]
                    self.cube['F'][i][0] = u[i]
                    self.cube['B'][i][2] = d[2-i]

            elif direction == "counterclockwise":
                for i in range(3):
                    self.cube['U'][i][0] = f[i]
                    self.cube['D'][2-i][0] = b[i]
                    self.cube['F'][i][0] = d[i]
                    self.cube['B'][i][2] = u[2-i]
            
        elif face == 'R':
            u = [self.cube['U'][i][2] for i in range(3)]
            d = [self.cube['D'][i][2] for i in range(3)]
            f = [self.cube['F'][i][2] for i in range(3)]
            b = [self.cube['B'][i][0] for i in range(3)]
            
            if direction == "clockwise":
                for i in range(3):
                    self.cube['U'][i][2] = f[i]
                    self.cube['D'][i][2] = b[2-i]
                    self.cube['F'][i][2] = d[i]
                    self.cube['B'][i][0] = u[2-i]

            elif direction == "counterclockwise":
                for i in range(3):
                    self.cube['U'][2-i][2] = b[i]
                    self.cube['D'][i][2] = f[i]
                    self.cube['F'][i][2] = u[i]
                    self.cube['B'][i][0] = d[2-i]
        
                
                
    def rotate(self, move):
        # Mapare miscari la Fata si directie
        move_map = {
            "U": ("U", "clockwise"),
            "D": ("D", "clockwise"),
            "F": ("F", "clockwise"),
            "B": ("B", "clockwise"),
            "L": ("L", "clockwise"),
            "R": ("R", "clockwise"),
            "U-": ("U", "counterclockwise"),
            "D-": ("D", "counterclockwise"),
            "F-": ("F", "counterclockwise"),
            "B-": ("B", "counterclockwise"),
            "L-": ("L", "counterclockwise"),
            "R-": ("R", "counterclockwise"),
        }
        if move in move_map:
            face, direction = move_map[move]
            self.rotate_face(face, direction)
        else:
            raise ValueError("Input Error: Miscare invalida!")

    def display(self):
        # Afișează starea curentă a cubului Rubik
        print("Starea curentă a cubului Rubik:")
        for face, colors in self.cube.items():
            print(f"{face}:")
            for row in colors:
                print(" ".join(row))
            print()
    
    def display_cross(self):
        # Afișează starea curentă a cubului Rubik în format încrucișat
        print("Starea curentă a cubului Rubik (format încrucișat):")
        U = self.cube['U']
        D = self.cube['D']
        F = self.cube['F']
        B = self.cube['B']
        L = self.cube['L']
        R = self.cube['R']

        for i in range(3):
            print("      " + " ".join(U[i]))
        for i in range(3):
            print(" ".join(L[i]) + " " + " ".join(F[i]) + " " + " ".join(R[i]) + " " + " ".join(B[i]))
        for i in range(3):
            print("      " + " ".join(D[i]))
        print()



