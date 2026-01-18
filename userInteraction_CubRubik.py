import CubRubik 
import solve_CubRubik as solveKaciemba

def main():
    # Crearea unei instanțe a cubului Rubik
    cub = CubRubik.CubRubik()
    
    # Afișarea stării inițiale a cubului
    cub.display_cross()

    print("You can rotate the cube using commands like 'U', 'D', 'F', 'B', 'L', 'R' for clockwise rotations,"
    " and 'U-', 'D-', 'F-', 'B-', 'L-', 'R-' for counterclockwise rotations.")

    user_input = input("Enter your rotation command (or type 'exit' to quit): ")

    valid_moves = ["U", "D", "F", "B", "L", "R",
                   "U-", "D-", "F-", "B-", "L-", "R-"]
    
    attempts = 0
    max_attempts = 3  # Limit the number of attempts to prevent infinite loops

    try:
        while user_input.lower() != 'exit':
            if user_input not in valid_moves and user_input.lower() != 'solve':
                print("Invalid move. Please enter a valid rotation command or type 'exit' to quit.")
                user_input = input("Enter your rotation command (or type 'exit' to quit): ")
                attempts += 1
                if attempts > max_attempts:
                    print("Too many invalid attempts. Exiting the simulator.")
                    exit()
            elif user_input in valid_moves:
                cub.rotate(user_input)
                cub.display_cross()
                user_input = input("Enter your next rotation command (type 'solve' for solution or type 'exit' to quit): ")
                attempts = 0 # Reset attempts after a valid move
            elif user_input.lower() == 'solve':
                print("Solving the cube...")
                # Here you could implement a solving algorithm if desired.
                cub_state = convert_to_string(cub.cube)
                print("Current cube state:", cub_state)
                solution = solveKaciemba.solve_cube(cub_state)
                if solution:
                   print("Solution found:", solution, "\nNumber of moves:", len(solution))
                   #To be implemented: apply the solution moves to the cube
                   exit()
                else:
                    # In case of error or no solution found
                    print("No solution found.")
                    exit()
            else:
                print("Exiting the simulator. Goodbye!")
                exit()  
    except ValueError as e:
        print("Error Detected:", e)

    print("Exiting the simulator. Goodbye!")
    
def convert_to_string(cube):
    """
    Converts the cube's state to a string representation.
    Required by the Kociemba solver.
    """
    # Build the string in Kociemba order: U, R, F, D, L, B
    cube_str = str(cube['U']) + str(cube['R']) + str(cube['F']) + str(cube['D']) + str(cube['L']) + str(cube['B'])
    # Remove spaces, commas, and brackets for a cleaner output
    cube_str = cube_str.replace(" ", "").replace(",", "").replace("[", "").replace("]", "").replace("'", "")
    for i in range(1, 10):
        cube_str = cube_str.replace(str(i), "")

    return cube_str