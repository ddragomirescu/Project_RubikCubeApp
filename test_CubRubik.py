# test_CubRubik.py
import unittest
import CubRubik

class TestCubRubik(unittest.TestCase):
    def setUp(self):
        self.cub = CubRubik.CubRubik()

    def test_initial_cube_state(self):
        expected = {
            'U': [['U'] * 3 for _ in range(3)],
            'D': [['D'] * 3 for _ in range(3)],
            'F': [['F'] * 3 for _ in range(3)],
            'B': [['B'] * 3 for _ in range(3)],
            'L': [['L'] * 3 for _ in range(3)],
            'R': [['R'] * 3 for _ in range(3)]
        }
        self.assertEqual(self.cub.cube, expected)

    def test_rotate_clockwise(self):
        # To do - implement a test for clockwise rotation
        return None
    
    def test_rotate_counterclockwise(self):
        # To do - implement a test for counterclockwise rotation
        return None

    def test_rotate_valid_moves(self):
        valid_moves = ["U", "D", "F", "B", "L", "R",
                       "U-", "D-", "F-", "B-", "L-", "R-"]
        for move in valid_moves:
            with self.subTest(move=move):
                self.cub.rotate(move)

    def test_rotate_invalid_move(self):
        with self.assertRaises(ValueError):
            self.cub.rotate("Input Error: Miscare invalida!")

    def test_display(self):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.cub.display()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("Starea curentă a cubului Rubik:", output)
        self.assertIn("U:", output)
        self.assertIn("D:", output)
        self.assertIn("F:", output)
        self.assertIn("B:", output)
        self.assertIn("L:", output)
        self.assertIn("R:", output)

if __name__ == '__main__':
    unittest.main() 

# test_CubRubik.py
# This file contains unit tests for the CubRubik class.