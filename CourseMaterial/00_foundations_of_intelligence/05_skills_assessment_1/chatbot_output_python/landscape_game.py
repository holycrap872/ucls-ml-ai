import math
import random

from .screen import Context, get_click_location

ctx = Context()
width = ctx.width
height = ctx.height
landscape = []


def generate_landscape():
    """
    Function to generate a random landscape with mountains and valleys
    """
    for i in range(0, width):
        # Create height with random variation, simulating mountains and valleys
        landscape.append(math.sin(i * 0.02) * 100 + random.random() * 50 + height / 2)

    max_peak = max(landscape)  # Find the tallest peak
    return max_peak


def reveal_slice(x):
    """
    Function to reveal a vertical slice of the landscape where clicked
    """
    ctx.clear_rect(x, 0, 1, height)
    ctx.begin_path()
    for i in range(-5, 5):
        ctx.move_to(x + i, height)
        ctx.line_to(x + i, landscape[x + i])
        ctx.stroke()


def handle_click(event, max_peak):
    """
    Function to handle clicks on the canvas
    """
    x = event.offset_x
    reveal_slice(x)

    # Check if the revealed slice is the tallest peak
    for i in range(-5, 5):
        if landscape[x + i] == max_peak:
            return True

    return False


def init():
    """
    Function to initialize the game
    """
    max_peak = generate_landscape()

    guesses = 0
    found_peak = False
    while not found_peak:
        event = get_click_location()

        found_peak = handle_click(event, max_peak)
        if found_peak:
            # Stop further clicks
            print("You found the peak after", guesses, "guesses!")
        else:
            print("Try again!")
            guesses += 1


if __name__ == "__main__":
    init()
