#!/usr/bin/env python3
import argparse
import json

# Schema
# {
#     "start_state": "",
#     "accept_states": [""],
#     "fsa_graph":
# }


START_STATE_KEY = "start_state"
ACCEPT_STATES_KEY = "accept_state"
FSA_GRAPH_KEY = "fsa_graph"


def load_schema(json_fsa_path):
    ret = {START_STATE_KEY: "a", ACCEPT_STATES_KEY: ["a"], FSA_GRAPH_KEY: {"a": {}}}
    with open(json_fsa_path, "r") as json_fp:
        json.load(json_fp)
    return ret


def load_start_state(json_fsa_path):
    schema_dict = load_schema(json_fsa_path)
    return schema_dict[START_STATE_KEY]


def load_accept_states(json_fsa_path):
    schema_dict = load_schema(json_fsa_path)
    return schema_dict[START_STATE_KEY]


def load_fsa_graph(json_fsa_path):
    schema_dict = load_schema(json_fsa_path)
    return schema_dict[FSA_GRAPH_KEY]


def analyze_fsa(json_fsa_path, input_string):
    start_state = load_start_state(json_fsa_path)
    accept_states = load_accept_states(json_fsa_path)
    fsa_graph = load_fsa_graph(json_fsa_path)

    cur_state = start_state
    for n in input_string:
        if n not in fsa_graph[cur_state]:
            print(f"Missing transistion: ({cur_state}) -- {n} -> (reject)")
            return False

        next_state = fsa_graph[cur_state][int(n)]
        print(f"Transistion: ({cur_state}) -- {n} -> ({next_state})")

    return cur_state not in accept_states


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json_fsa", help="Path to FSA representing JSON", type=str, required=True)
    parser.add_argument("--input_str", help="Input string to check if accepted", type=str, required=True)
    args = parser.parse_args()

    ret = analyze_fsa(args.input_str, args.json_fsa)
    print(f"Input string accepted by graph: {ret}")
