// Global variable to store current solution
let currentSolution = [];

// Convert Kociemba notation to our notation
// U' -> U-, U2 -> U U
function convertMove(move) {
    // Handle prime notation (counter-clockwise)
    if (move.includes("'")) {
        return [move.replace("'", "-")];
    }
    // Handle double turns (U2 -> U U)
    if (move.includes("2")) {
        const face = move.replace("2", "");
        return [face, face];
    }
    // Regular move
    return [move];
}

// Convert solution array to our notation
function convertSolution(solution) {
    const converted = [];
    solution.forEach(move => {
        const convertedMoves = convertMove(move);
        converted.push(...convertedMoves);
    });
    return converted;
}

// Initialize cube on page load
document.addEventListener('DOMContentLoaded', function() {
    updateCubeDisplay();
});

// Update cube display from server
async function updateCubeDisplay() {
    try {
        const response = await fetch('/api/cube');
        const data = await response.json();
        renderCube(data);
    } catch (error) {
        console.error('Error updating cube display:', error);
        showError('Failed to update cube display');
    }
}

// Render cube with colors
function renderCube(cubeData) {
    const faces = ['U', 'D', 'F', 'B', 'L', 'R'];

    faces.forEach(face => {
        const faceData = cubeData[face];
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                const color = faceData[i][j];

                // Update 2D cross view
                const cell = document.querySelector(
                    `.cell[data-face="${face}"][data-pos="${i}-${j}"]`
                );
                if (cell) {
                    cell.setAttribute('data-color', color);
                }

                // Update 3D cube view
                const cell3d = document.querySelector(
                    `.cell-3d[data-face="${face}"][data-pos="${i}-${j}"]`
                );
                if (cell3d) {
                    cell3d.setAttribute('data-color', color);
                }
            }
        }
    });
}

// Rotate cube
async function rotateCube(move) {
    showLoading();
    try {
        const response = await fetch('/api/rotate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ move: move })
        });

        const data = await response.json();
        hideLoading();

        if (data.success) {
            renderCube(data.cube);
        } else {
            showError(data.error || 'Failed to rotate cube');
        }
    } catch (error) {
        hideLoading();
        console.error('Error rotating cube:', error);
        showError('Failed to rotate cube');
    }
}

// Reset cube
async function resetCube() {
    showLoading();
    try {
        const response = await fetch('/api/reset', {
            method: 'POST'
        });

        const data = await response.json();
        hideLoading();

        if (data.success) {
            renderCube(data.cube);
            hideSolution();
            showSuccess('Cube reset to solved state!');
        } else {
            showError('Failed to reset cube');
        }
    } catch (error) {
        hideLoading();
        console.error('Error resetting cube:', error);
        showError('Failed to reset cube');
    }
}

// Scramble cube
async function scrambleCube() {
    showLoading();
    try {
        const response = await fetch('/api/scramble', {
            method: 'POST'
        });

        const data = await response.json();
        hideLoading();

        if (data.success) {
            renderCube(data.cube);
            hideSolution();
            showSuccess(`Cube scrambled with ${data.scramble.length} moves!`);
        } else {
            showError('Failed to scramble cube');
        }
    } catch (error) {
        hideLoading();
        console.error('Error scrambling cube:', error);
        showError('Failed to scramble cube');
    }
}

// Solve cube
async function solveCube() {
    showLoading();
    try {
        const response = await fetch('/api/solve', {
            method: 'POST'
        });

        const data = await response.json();
        hideLoading();

        if (data.success) {
            currentSolution = data.solution;
            displaySolution(data.solution, data.steps, data.cube_notation);
        } else {
            showError(data.error || 'Invalid cube configuration, please try again');
        }
    } catch (error) {
        hideLoading();
        console.error('Error solving cube:', error);
        showError('Invalid cube configuration, please try again');
    }
}

// Display solution
function displaySolution(solution, steps, cubeNotation) {
    const solutionSection = document.getElementById('solution-section');
    const stepsElement = document.getElementById('solution-steps');
    const movesListElement = document.getElementById('solution-moves-list');
    const notationElement = document.getElementById('cube-notation-string');

    stepsElement.textContent = steps;
    movesListElement.innerHTML = '';

    solution.forEach(move => {
        const moveBadge = document.createElement('span');
        moveBadge.className = 'move-badge';
        moveBadge.textContent = move;
        movesListElement.appendChild(moveBadge);
    });

    // Display cube notation if provided
    if (cubeNotation) {
        notationElement.textContent = cubeNotation;
    }

    solutionSection.style.display = 'block';
    solutionSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Hide solution
function hideSolution() {
    const solutionSection = document.getElementById('solution-section');
    solutionSection.style.display = 'none';
    currentSolution = [];
}

// Apply solution (execute all moves)
async function applySolution() {
    if (currentSolution.length === 0) {
        showError('No solution to apply');
        return;
    }

    showLoading();

    try {
        // Convert solution to our notation
        const convertedSolution = convertSolution(currentSolution);
        console.log('Original solution:', currentSolution);
        console.log('Converted solution:', convertedSolution);

        for (let i = 0; i < convertedSolution.length; i++) {
            const move = convertedSolution[i];
            const response = await fetch('/api/rotate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ move: move })
            });

            const data = await response.json();

            if (data.success) {
                renderCube(data.cube);
                // Small delay to see the animation
                await new Promise(resolve => setTimeout(resolve, 300));
            } else {
                hideLoading();
                showError(`Failed at move ${i + 1}: ${move}`);
                return;
            }
        }

        hideLoading();
        showSuccess('Solution applied successfully!');
        hideSolution();
    } catch (error) {
        hideLoading();
        console.error('Error applying solution:', error);
        showError('Failed to apply solution');
    }
}

// Show loading indicator
function showLoading() {
    document.getElementById('loading').style.display = 'block';
}

// Hide loading indicator
function hideLoading() {
    document.getElementById('loading').style.display = 'none';
}

// Show error message
function showError(message) {
    alert('Error: ' + message);
}

// Show success message
function showSuccess(message) {
    alert(message);
}

// View switching
let currentView = 'cross';

function switchView(view) {
    const crossView = document.getElementById('cross-view');
    const view3d = document.getElementById('3d-view');
    const buttons = document.querySelectorAll('.btn-view');

    if (view === 'cross') {
        crossView.style.display = 'flex';
        view3d.style.display = 'none';
        currentView = 'cross';
    } else {
        crossView.style.display = 'none';
        view3d.style.display = 'flex';
        currentView = '3d';
        // Update 3D cube when switching to 3D view
        updateCube3D();
    }

    // Update button states
    buttons.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');
}

// Update 3D cube display
function updateCube3D() {
    const faces = ['U', 'D', 'F', 'B', 'L', 'R'];
    
    faces.forEach(face => {
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                const cell2d = document.querySelector(
                    `.cell[data-face="${face}"][data-pos="${i}-${j}"]`
                );
                const cell3d = document.querySelector(
                    `.cell-3d[data-face="${face}"][data-pos="${i}-${j}"]`
                );
                
                if (cell2d && cell3d) {
                    const color = cell2d.getAttribute('data-color');
                    cell3d.setAttribute('data-color', color);
                }
            }
        }
    });
}

// 3D Cube Rotation with Mouse
let isDragging = false;
let previousMousePosition = { x: 0, y: 0 };
let rotation = { x: -20, y: -30 };

const cube3d = document.getElementById('cube-3d');
const cube3dContainer = document.querySelector('.cube-3d-container');

if (cube3dContainer) {
    cube3dContainer.addEventListener('mousedown', (e) => {
        isDragging = true;
        previousMousePosition = { x: e.clientX, y: e.clientY };
    });

    document.addEventListener('mousemove', (e) => {
        if (!isDragging || currentView !== '3d') return;

        const deltaX = e.clientX - previousMousePosition.x;
        const deltaY = e.clientY - previousMousePosition.y;

        rotation.y += deltaX * 0.5;
        rotation.x -= deltaY * 0.5;

        cube3d.style.transform = `rotateX(${rotation.x}deg) rotateY(${rotation.y}deg)`;

        previousMousePosition = { x: e.clientX, y: e.clientY };
    });

    document.addEventListener('mouseup', () => {
        isDragging = false;
    });

    // Touch support for mobile
    cube3dContainer.addEventListener('touchstart', (e) => {
        isDragging = true;
        previousMousePosition = {
            x: e.touches[0].clientX,
            y: e.touches[0].clientY
        };
    });

    document.addEventListener('touchmove', (e) => {
        if (!isDragging || currentView !== '3d') return;

        const deltaX = e.touches[0].clientX - previousMousePosition.x;
        const deltaY = e.touches[0].clientY - previousMousePosition.y;

        rotation.y += deltaX * 0.5;
        rotation.x -= deltaY * 0.5;

        cube3d.style.transform = `rotateX(${rotation.x}deg) rotateY(${rotation.y}deg)`;

        previousMousePosition = {
            x: e.touches[0].clientX,
            y: e.touches[0].clientY
        };
    });

    document.addEventListener('touchend', () => {
        isDragging = false;
    });
}
