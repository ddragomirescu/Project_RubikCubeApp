# test_CubRubik.py
import unittest
import CubRubik

class TestCubRubik(unittest.TestCase):
    def setUp(self):
        self.cub = CubRubik.CubRubik()

    def test_initial_cube_state(self):
        expected = {
            'Sus': [['Alb'] * 3 for _ in range(3)],
            'Jos': [['Galben'] * 3 for _ in range(3)],
            'Fata': [['Rosu'] * 3 for _ in range(3)],
            'Spate': [['Portocaliu'] * 3 for _ in range(3)],
            'Stanga': [['Verde'] * 3 for _ in range(3)],
            'Dreapta': [['Albastru'] * 3 for _ in range(3)]
        }
        self.assertEqual(self.cub.cube, expected)

    def test_rotate_face_clockwise(self):
        self.cub.rotate_face('Sus')
        self.assertNotEqual(self.cub.cube['Sus'], [['Alb'] * 3 for _ in range(3)])

    def test_rotate_face_counterclockwise(self):
        self.cub.rotate_face('Sus', 'counterclockwise')
        self.assertNotEqual(self.cub.cube['Sus'], [['Alb'] * 3 for _ in range(3)])

    def test_rotate_valid_moves(self):
        valid_moves = ["Sus", "Jos", "Fata", "Spate", "Stanga", "Dreapta",
                       "Sus'", "Jos'", "Fata'", "Spate'", "Stanga'", "Dreapta'"]
        for move in valid_moves:
            with self.subTest(move=move):
                self.cub.rotate(move)

    def test_rotate_invalid_move(self):
        with self.assertRaises(ValueError):
            self.cub.rotate("InvalidMove")

    def test_display(self):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.cub.display()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Starea curentă a cubului Rubik:", output)
        self.assertIn("Sus:", output)
        self.assertIn("Jos:", output)
        self.assertIn("Fata:", output)
        self.assertIn("Spate:", output)
        self.assertIn("Stanga:", output)
        self.assertIn("Dreapta:", output)

if __name__ == '__main__':
    unittest.main() 

# test_CubRubik.py
# This file contains unit tests for the CubRubik class.