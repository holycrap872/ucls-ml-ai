#!/usr/bin/env python3


def remove_character(word: str) -> None:
    if len(word) == 0:
        return

    remove_character(word[1:])
    print(word[0])


# remove_character("")
# remove_character("hi")
remove_character("Hello!")
