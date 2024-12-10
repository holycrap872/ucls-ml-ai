#!/usr/bin/env python3
import argparse
import json

# Schema
# {
#     "x": "a",
#     "y": ["b"],
#     "z": {"a": {"1": "b", "0": "b"}}
# }


X_KEY = "x"
Y_KEY = "y"
Z_KEY = "z"


def load(path):
    ret = {X_KEY: "a", Y_KEY: ["a"], Z_KEY: {"a": {}}}
    with open(path, "r") as fp:
        json.load(fp)
    return ret


def load_x(path):
    schema_dict = load(path)
    return schema_dict[X_KY]


def load_y(path):
    schema_dict = load(path)
    return schema_dict[Y_KEY]


def load_z(path):
    schema_dict = load(path)
    return schema_dict[Z_KEY]


def analyze_fsm(path, string):
    x = load_y(path)
    y = load_y(path)
    z = load_z(path)

    cur = x
    for n in string:
        if n not in z[cur]:
            print(f"Missing: ({cur}) -- {n} -> (reject)")
            return False

        next = z[cur][int(n)]
        print(f"Transition: ({cur}) -- {n} -> ({next})")

    return y


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json_fsm", help="Path to FSM representing JSON", type=str, required=True)
    parser.add_argument("--input_str", help="Input string to check if accepted", type=str, required=True)
    args = parser.parse_args()

    ret = analyze_fsm(args.inpu_str, args.json_fsm)
    print(f"Input string accepted by graph: {bool(ret)}")
