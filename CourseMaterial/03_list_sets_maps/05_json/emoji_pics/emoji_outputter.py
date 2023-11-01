#!/usr/bin/env python3
import json
import typing


def encoding_to_emoji(encoding: str) -> str:
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

    return MAP[encoding]


def output_picture(picture: typing.Dict[str, typing.List[str]]) -> None:
    for i in range(len(picture)):
        row = picture[str(i)]

        output_str = ""
        for encoding in row:
            output_str += encoding_to_emoji(encoding)

        print(output_str)


def load_picture(path: str) -> typing.Dict:
    with open(path, "r") as fp:
        return json.load(fp)


def emoji_outputter() -> None:
    encoded_picture = load_picture("CourseMaterial/03_list_sets_maps/05_json/emoji_pics/flag.json")
    output_picture(encoded_picture)


if __name__ == "__main__":
    emoji_outputter()
