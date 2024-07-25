#!/usr/bin/env python3
import typing


class GuessNode(typing.NamedTuple):
    guess: str
    yes_node: typing.Optional["GuessNode"]
    no_node: typing.Optional["GuessNode"]


# Guessing between Joe and Ben
def play_guess_who() -> None:
    joe = GuessNode("Is it Joe? ", None, None)
    ben = GuessNode("Is it Ben? ", None, None)

    root = GuessNode("Are they bald? ", yes_node=joe, no_node=ben)

    guess_node = root
    while guess_node != None:
        answer = input(guess_node.guess)
        if answer.lower() == "yes":
            guess_node = guess_node.yes_node
        else:
            guess_node = guess_node.no_node

    final_answer = answer
    if final_answer.lower() == "yes":
        print("I got it!")
    else:
        print("Oh no, I guessed wrong!")


if __name__ == "__main__":
    play_guess_who()
