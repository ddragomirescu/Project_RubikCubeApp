# test_CubRubik.py
import unittest
import CubRubik

class TestCubRubik(unittest.TestCase):
    def setUp(self):
        self.cub = CubRubik.CubRubik()

    def test_initial_cube_state(self):
        expected = {
            'U': [['W'] * 3 for _ in range(3)],
            'D': [['Y'] * 3 for _ in range(3)],
            'F': [['R'] * 3 for _ in range(3)],
            'B': [['O'] * 3 for _ in range(3)],
            'L': [['G'] * 3 for _ in range(3)],
            'R': [['B'] * 3 for _ in range(3)]
        }
        self.assertEqual(self.cub.cube, expected)

    def test_rotate_clockwise(self):
        self.cub.rotate("U")
        # The following expected dict has syntax errors in list construction.
        # Correct syntax for combining lists:
        # [item1] + [item2 for _ in range(n)]
        # But for a face, you want a 3x3 grid, so [['color'] * 3 for _ in range(3)]
        # If you want to change only the first row, use:
        # [new_row] + [original_row for _ in range(2)]
        # Example for 'F': [['B'] * 3] + [['R'] * 3 for _ in range(2)]
        expected = {
            'U': [['W'] * 3 for _ in range(3)],
            'D': [['Y'] * 3 for _ in range(3)],
            'F': [['B'] * 3] + [['R'] * 3 for _ in range(2)],
            'B': [['G'] * 3] + [['O'] * 3 for _ in range(2)],
            'L': [['R'] * 3] + [['G'] * 3 for _ in range(2)],
            'R': [['O'] * 3] + [['B'] * 3 for _ in range(2)]
        }
        self.assertEqual(self.cub.cube, expected)

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