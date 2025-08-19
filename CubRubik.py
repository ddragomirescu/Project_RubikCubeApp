class CubRubik:
    def __init__(self):
        self.cube = self.gen_cube()

    def gen_cube(self):  
        # Genereaza un cub Rubik 3x3x3 cu culori initiale
        return {
            'U': [['W']        * 3 for index in range(3)],
            'D': [['Y']     * 3 for index in range(3)],
            'F': [['R']       * 3 for index in range(3)],
            'B': [['O'] * 3 for index in range(3)],
            'L': [['G']      * 3 for index in range(3)],
            'R': [['B']   * 3 for index in range(3)]
        }

    def rotate_face(self, face, direction="clockwise"):
        # Rotatie F cubului cu 90 de grade in sensul accelor de ceasornic 
        if direction == "clockwise":
            self.cube[face] = [list(row) for row in zip(*self.cube[face][::-1])]
        elif direction == "counterclockwise":
            # Rotatie F cubului cu 90 de grade in sens trigonometric
            self.cube[face] = [list(row) for row in zip(*self.cube[face])][::-1]

        # Roatirea marginilor adiacente
        if face == 'U':
            if direction == "clockwise":  
                temp = self.cube['F'][0][:]
                self.cube['F'][0] = self.cube['R'][0][::-1]
                self.cube['R'][0] = self.cube['B'][0][:]
                self.cube['B'][0] = self.cube['L'][0][:]
                self.cube['L'][0] = temp
            elif direction == "counterclockwise":
                temp = self.cube['F'][0][:]
                self.cube['F'][0] = self.cube['L'][0][:]
                self.cube['L'][0] = self.cube['B'][0][::-1]
                self.cube['B'][0] = self.cube['R'][0][::-1]
                self.cube['R'][0] = temp
        elif face == 'D':
            if direction == "clockwise":
                temp = self.cube['F'][2][:]
                self.cube['F'][2] = self.cube['L'][2][::-1]
                self.cube['L'][2] = self.cube['B'][2][:]
                self.cube['B'][2] = self.cube['R'][2][:]
                self.cube['R'][2] = temp
            elif direction == "counterclockwise":
                temp = self.cube['F'][2][:]
                self.cube['F'][2] = self.cube['R'][2][::-1]
                self.cube['R'][2] = self.cube['B'][2][:]
                self.cube['B'][2] = self.cube['L'][2][:]
                self.cube['L'][2] = temp
        elif face == 'F':
            if direction == "clockwise":
                temp = [self.cube['U'][2][i] for i in range(3)]
                for i in range(3):
                    self.cube['U'][2][i] = self.cube['L'][2-i][2]
                    self.cube['L'][2-i][2] = self.cube['D'][0][i]
                    self.cube['D'][0][i] = self.cube['R'][i][0]
                    self.cube['R'][i][0] = temp[i]
            elif direction == "counterclockwise":
                temp = [self.cube['U'][2][i] for i in range(3)]
                for i in range(3):
                    self.cube['U'][2][i] = self.cube['R'][i][0]
                    self.cube['R'][i][0] = self.cube['D'][0][i]
                    self.cube['D'][0][i] = self.cube['L'][2-i][2]
                    self.cube['L'][2-i][2] = temp[i]
        elif face == 'B':
            if direction == "clockwise":
                temp = [self.cube['U'][0][i] for i in range(3)]
                for i in range(3):
                    self.cube['U'][0][i] = self.cube['R'][2-i][2]
                    self.cube['R'][2-i][2] = self.cube['D'][2][i]
                    self.cube['D'][2][i] = self.cube['L'][i][0]
                    self.cube['L'][i][0] = temp[i]
            elif direction == "counterclockwise":
                temp = [self.cube['U'][0][i] for i in range(3)]
                for i in range(3):
                    self.cube['U'][0][i] = self.cube['L'][i][0]
                    self.cube['L'][i][0] = self.cube['D'][2][i]
                    self.cube['D'][2][i] = self.cube['R'][2-i][2]
                    self.cube['R'][2-i][2] = temp[i]
        elif face == 'L':
            if direction == "clockwise":
                temp = [self.cube['U'][i][0] for i in range(3)]
                for i in range(3):
                    self.cube['U'][i][0] = self.cube['B'][2-i][2]
                    self.cube['B'][2-i][2] = self.cube['D'][2-i][0]
                    self.cube['D'][2-i][0] = self.cube['F'][i][0]
                    self.cube['F'][i][0] = temp[i]
            elif direction == "counterclockwise":
                temp = [self.cube['U'][i][0] for i in range(3)]
                for i in range(3):
                    self.cube['U'][i][0] = self.cube['F'][i][0]
                    self.cube['F'][i][0] = self.cube['D'][2-i][0]
                    self.cube['D'][2-i][0] = self.cube['B'][2-i][2]
                    self.cube['B'][2-i][2] = temp[i]
        elif face == 'R':
            if direction == "clockwise":
                temp = [self.cube['U'][i][2] for i in range(3)]
                for i in range(3):
                    self.cube['U'][i][2] = self.cube['F'][i][2]
                    self.cube['F'][i][2] = self.cube['D'][i][2]
                    self.cube['D'][i][2] = self.cube['B'][2-i][0]
                    self.cube['B'][2-i][0] = temp[i]                
            elif direction == "counterclockwise":
                temp = [self.cube['U'][i][2] for i in range(3)]
                for i in range(3):
                    self.cube['U'][i][2] = self.cube['B'][2-i][0]
                    self.cube['B'][2-i][0] = self.cube['D'][i][2]
                    self.cube['D'][i][2] = self.cube['F'][i][2]
                    self.cube['F'][i][2] = temp[i]
                
                
    def rotate(self, move):
        # Mapare miscari la F si directie
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



