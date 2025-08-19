class CubRubik:
    def __init__(self):
        self.cube = self.gen_cube()

    def gen_cube(self):  
        # Genereaza un cub Rubik 3x3x3 cu culori initiale
        return {
            'Sus'    : [['Alb']        * 3 for index in range(3)],
            'Jos'    : [['Galben']     * 3 for index in range(3)],
            'Fata'   : [['Rosu']       * 3 for index in range(3)],
            'Spate'  : [['Portocaliu'] * 3 for index in range(3)],
            'Stanga' : [['Verde']      * 3 for index in range(3)],
            'Dreapta': [['Albastru']   * 3 for index in range(3)]
        }

    def rotate_face(self, face, direction='clockwise'):
        # Rotatie fata cubului cu 90 de grade in sensul accelor de ceasornic 
        if direction == 'clockwise':
            self.cube[face] = [list(row) for row in zip(*self.cube[face][::-1])]
        elif direction == 'counterclockwise':
            # Rotatie fata cubului cu 90 de grade in sens trigonometric
            self.cube[face] = [list(row) for row in zip(*self.cube[face])][::-1]   

    def rotate(self, move):
        # Mapare miscari la fata si directie
        move_map = {
            "Sus":      ("Sus", "clockwise"),
            "Jos":      ("Jos", "clockwise"),
            "Fata":     ("Fata", "clockwise"),
            "Spate":    ("Spate", "clockwise"),
            "Stanga":   ("Stanga", "clockwise"),
            "Dreapta":  ("Dreapta", "clockwise"),
            "Sus-":     ("Sus", "counterclockwise"),
            "Jos-":     ("Jos", "counterclockwise"),
            "Fata-":    ("Fata", "counterclockwise"),
            "Spate-":   ("Spate", "counterclockwise"),
            "Stanga-":  ("Stanga", "counterclockwise"),
            "Dreapta-": ("Dreapta", "counterclockwise"),
        }
        if move in move_map:
            face, direction = move_map[move]
            self.rotate_face(face, direction)
        else:
            raise ValueError("Miscare invalida! " + move)

    def display(self):
        # Afișează starea curentă a cubului Rubik
        print("Starea curentă a cubului Rubik:")
        for face, colors in self.cube.items():
            print(f"{face}:")
            for row in colors:
                print(" ".join(row))
            print()



