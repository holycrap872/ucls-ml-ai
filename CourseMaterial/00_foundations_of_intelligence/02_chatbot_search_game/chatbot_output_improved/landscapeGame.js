const canvas = document.getElementById('landscapeCanvas');
const ctx = canvas.getContext('2d');
const guessCountElement = document.getElementById('guessCount');

const width = canvas.width;
const height = canvas.height;

let landscape = [];
let maxPeak = 0;
let guesses = 0;

// Function to generate a random landscape with mountains and valleys
function generateLandscape() {
    const peaks = 10; // Number of peaks in the landscape
    for (let i = 0; i < width; i++) {
        // Create height with random variation, simulating mountains and valleys
        landscape[i] = Math.sin(i * 0.02) * 100 + Math.random() * 10 + height / 2;
    }
    maxPeak = Math.min(...landscape); // Find the tallest peak
}

// Function to draw the landscape covered by black screen
function drawLandscape() {
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, width, height);
}

// Function to reveal a vertical slice of the landscape where clicked
function revealSlice(x) {
    ctx.clearRect(x, 0, 1, height);
    ctx.beginPath();
    for (let i = -5; i < 5; i++) {
        ctx.moveTo(x + i, height);
        ctx.lineTo(x + i, landscape[x + i]);
        ctx.strokeStyle = 'green';
        ctx.stroke();
    }
}

// Function to handle clicks on the canvas
function handleClick(event) {
    const x = event.offsetX;
    revealSlice(x);

    guesses += 1;
    guessCountElement.textContent = guesses;

    // Check if the revealed slice is the tallest peak
    for (let i = -5; i < 5; i ++) {
        if (landscape[x + i] === maxPeak) {
            alert(`You've found the tallest peak in ${guesses} guesses!`);
            canvas.removeEventListener('click', handleClick); // Stop further clicks
        }
    }
}

// Initialize the game
function init() {
    generateLandscape();
    drawLandscape();
    canvas.addEventListener('click', handleClick);
}

init();