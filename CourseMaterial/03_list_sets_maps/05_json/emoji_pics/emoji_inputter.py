#!/usr/bin/env python3
import json


def emoji_to_bits(emoji: str) -> str:
    MAP = {
        "⬛": "000",
        "🟥": "100",
        "🟩": "010",
        "🟦": "001",
        "🟨": "110",
        "🟪": "101",
        "🩵": "011",
        "⬜": "111",
    }

    if emoji not in MAP:
        return ""
    return MAP[emoji]


def load_data_from_file(path: str) -> str:
    with open(path, "r") as fp:
        return fp.read()


def output_json(data: str) -> None:
    ret: dict[str, list[str]] = {}
    for line_num, line in enumerate(data.split("\n")):
        row: list[str] = []
        for emoji in line:
            encoding = emoji_to_bits(emoji)
            if encoding:
                row.append(encoding)
        ret[str(line_num)] = row

    print(json.dumps(ret))


if __name__ == "__main__":
    data = load_data_from_file("CourseMaterial/03_list_sets_maps/05_json/emoji_pics/color_mario.txt")
    output_json(data)
