# Rubik's Cube Solver Web App

A beautiful web application built with Flask for visualizing and solving Rubik's Cube puzzles using the Kociemba algorithm.

## Features

- **Interactive Cube Visualization**: View the cube in cross/net form with color-coded faces
- **Rotation Controls**: Execute R, L, U, D, F, B moves (both clockwise and counter-clockwise)
- **Reset Function**: Return cube to solved state
- **Scramble Function**: Randomly scramble the cube
- **Solve Function**: Get step-by-step solution using Kociemba algorithm
- **Apply Solution**: Watch the cube solve itself automatically

## Cube Face Colors

- **U (Up/Top)**: White
- **D (Down/Bottom)**: Yellow
- **F (Front)**: Green
- **B (Back)**: Blue
- **L (Left)**: Orange
- **R (Right)**: Red

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## How to Use

1. **Rotate the Cube**: Click on the move buttons (R, L, U, D, F, B) to rotate faces
   - Regular buttons = clockwise rotation
   - Buttons with apostrophe (') = counter-clockwise rotation

2. **Scramble**: Click "Scramble" to randomize the cube

3. **Solve**: Click "Solve" to generate a solution
   - View the number of steps required
   - See all the moves needed to solve the cube
   - Click "Apply Solution" to watch it solve automatically

4. **Reset**: Click "Reset" to return to the solved state

## Project Structure

```
Project_RubikCubeApp/
├── app.py                      # Flask application
├── CubRubik.py                 # Cube logic
├── solve_CubRubik.py           # Kociemba solver
├── userInteraction_CubRubik.py # Helper functions
├── templates/
│   └── index.html              # Main web page
├── static/
│   ├── style.css               # Styling
│   └── script.js               # Frontend logic
└── requirements.txt            # Python dependencies
```

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Solver**: Kociemba algorithm
- **Styling**: Custom CSS with gradients and animations

## Notes

- The Kociemba algorithm provides optimal or near-optimal solutions
- Solution typically ranges from 15-25 moves
- The cube state is maintained on the server side
- All rotations and solutions are computed in real-time
