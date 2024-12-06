#!/usr/bin/env python3
import json


def load_dict_from_file(path: str) -> dict:
    with open(path, "r") as fp:
        return json.loads(fp.read())


def bits_to_emoji(pixel_bits: str) -> str:
    MAP = {
        "000": "⬛️",
        "100": "🟥",
        "010": "🟩",
        "001": "🟦",
        "110": "🟨",
        "101": "🟪",
        "011": "🩵",
        "111": "⬜️",
    }

    return MAP[pixel_bits]


def emoji_outputter() -> None:
    encoded_picture = load_dict_from_file("CourseMaterial/03_list_sets_maps/05_json/emoji_pics/color_mario.json")
    for i in range(len(encoded_picture)):
        row = encoded_picture[str(i)]

        output_str = ""
        for pixel in row:
            output_str += bits_to_emoji(pixel)

        print(output_str)


if __name__ == "__main__":
    emoji_outputter()
