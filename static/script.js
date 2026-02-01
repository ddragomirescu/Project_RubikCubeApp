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
                const cell = document.querySelector(
                    `.cell[data-face="${face}"][data-pos="${i}-${j}"]`
                );
                if (cell) {
                    const color = faceData[i][j];
                    cell.setAttribute('data-color', color);
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
            displaySolution(data.solution, data.steps);
        } else {
            showError(data.error || 'Failed to solve cube');
        }
    } catch (error) {
        hideLoading();
        console.error('Error solving cube:', error);
        showError('Failed to solve cube');
    }
}

// Display solution
function displaySolution(solution, steps) {
    const solutionSection = document.getElementById('solution-section');
    const stepsElement = document.getElementById('solution-steps');
    const movesListElement = document.getElementById('solution-moves-list');

    stepsElement.textContent = steps;
    movesListElement.innerHTML = '';

    solution.forEach(move => {
        const moveBadge = document.createElement('span');
        moveBadge.className = 'move-badge';
        moveBadge.textContent = move;
        movesListElement.appendChild(moveBadge);
    });

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
