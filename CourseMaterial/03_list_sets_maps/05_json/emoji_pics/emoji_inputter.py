#!/usr/bin/env python3
import json
import typing


def emoji_to_encoding(emoji: str) -> str:
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


def emoji_inputter(emoji_pic_path: str) -> None:
    ret = {}
    with open(emoji_pic_path) as fp:
        for line_num, line in enumerate(fp):
            row = []
            for emoji in line:
                encoding = emoji_to_encoding(emoji)
                if encoding:
                    row.append(encoding)
            ret[str(line_num)] = row

    print(json.dumps(ret))


if __name__ == "__main__":
    emoji_inputter("CourseMaterial/03_list_sets_maps/05_json/emoji_pics/whale.txt")
