import kociemba # dependency: pip install kociemba

def solve_cube(cube_string):
    """
    Solves the Rubik's Cube using the kociemba library.
    
    :param cube_string: A string representation of the cube state.
    :return: A list of moves to solve the cube.
    """
    try:
        solution = kociemba.solve(cube_string)
        return solution.split()
    except Exception as e:
        raise ValueError(f"Error solving the cube: {e}")