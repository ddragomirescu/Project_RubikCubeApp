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
            'steps': len(solution),
            'cube_notation': cube_state
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/set-cube', methods=['POST'])
def set_cube():
    """Set custom cube state from color config"""
    global cube
    try:
        data = request.get_json()
        custom_state = data.get('cube')

        if not custom_state:
            return jsonify({
                'success': False,
                'error': 'No cube state provided'
            }), 400

        # Validate that we have all 6 faces with 9 cells each
        required_faces = ['U', 'D', 'F', 'B', 'L', 'R']
        for face in required_faces:
            if face not in custom_state or len(custom_state[face]) != 3:
                return jsonify({
                    'success': False,
                    'error': 'Invalid cube configuration'
                }), 400
            for row in custom_state[face]:
                if len(row) != 3:
                    return jsonify({
                        'success': False,
                        'error': 'Invalid cube configuration'
                    }), 400

        # Create new cube with custom state
        cube = CubRubik.CubRubik()

        # Map colors back to cell identifiers (e.g., 'U' -> 'U1', 'U2', etc.)
        for face in required_faces:
            for i in range(3):
                for j in range(3):
                    color = custom_state[face][i][j]
                    # Set the color in the cube (color + position number)
                    cube.cube[face][i][j] = color + str(i * 3 + j + 1)

        return jsonify({
            'success': True,
            'cube': get_colored_state()
        })
    except Exception:
        return jsonify({
            'success': False,
            'error': 'Invalid cube configuration, please try again'
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

@app.route('/api/solve-notation', methods=['POST'])
def solve_from_notation():
    """Solve cube directly from notation string"""
    try:
        data = request.get_json()
        notation = data.get('notation')

        if not notation:
            return jsonify({
                'success': False,
                'error': 'No cube notation provided'
            }), 400

        # Validate notation length (should be 54 characters for a 3x3 cube)
        if len(notation) != 54:
            return jsonify({
                'success': False,
                'error': f'Invalid notation length. Expected 54 characters, got {len(notation)}.'
            }), 400

        # Solve the cube using the notation string
        solution = solveKociemba.solve_cube(notation)

        return jsonify({
            'success': True,
            'solution': solution,
            'steps': len(solution),
            'notation': notation
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
