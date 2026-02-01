from flask import Flask, render_template, jsonify, request
import CubRubik
import solve_CubRubik as solveKociemba
from userInteraction_CubRubik import convert_to_string

app = Flask(__name__)

# Global cube instance
cube = CubRubik.CubRubik()

def get_cube_state():
    """Convert cube state to a format suitable for the frontend"""
    return {
        'U': cube.cube['U'],
        'D': cube.cube['D'],
        'F': cube.cube['F'],
        'B': cube.cube['B'],
        'L': cube.cube['L'],
        'R': cube.cube['R']
    }

def get_face_colors(face_data):
    """Extract just the face letter from each cell (e.g., 'U1' -> 'U')"""
    return [[cell[0] for cell in row] for row in face_data]

def get_colored_state():
    """Get cube state with just the face letters for coloring"""
    state = get_cube_state()
    return {
        'U': get_face_colors(state['U']),
        'D': get_face_colors(state['D']),
        'F': get_face_colors(state['F']),
        'B': get_face_colors(state['B']),
        'L': get_face_colors(state['L']),
        'R': get_face_colors(state['R'])
    }

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/solver')
def solver():
    return render_template('solver.html')

@app.route('/guide')
def guide():
    return render_template('guide.html')

@app.route('/api/cube')
def get_cube():
    """Get current cube state"""
    return jsonify(get_colored_state())

@app.route('/api/rotate', methods=['POST'])
def rotate():
    """Rotate the cube based on the move"""
    data = request.get_json()
    move = data.get('move')

    try:
        cube.rotate(move)
        return jsonify({
            'success': True,
            'cube': get_colored_state()
        })
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/reset', methods=['POST'])
def reset():
    """Reset the cube to solved state"""
    global cube
    cube = CubRubik.CubRubik()
    return jsonify({
        'success': True,
        'cube': get_colored_state()
    })

@app.route('/api/solve', methods=['POST'])
def solve():
    """Solve the cube using Kociemba algorithm"""
    try:
        cube_state = convert_to_string(cube.cube)
        solution = solveKociemba.solve_cube(cube_state)

        return jsonify({
            'success': True,
            'solution': solution,
            'steps': len(solution)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/scramble', methods=['POST'])
def scramble():
    """Scramble the cube with random moves"""
    import random
    moves = ['U', 'D', 'F', 'B', 'L', 'R', 'U-', 'D-', 'F-', 'B-', 'L-', 'R-']
    scramble_moves = [random.choice(moves) for _ in range(20)]

    for move in scramble_moves:
        cube.rotate(move)

    return jsonify({
        'success': True,
        'cube': get_colored_state(),
        'scramble': scramble_moves
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
