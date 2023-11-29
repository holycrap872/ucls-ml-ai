#!/usr/bin/env python3
import argparse
import json

# Schema
# {
#     "start_state": "",
#     "accept_states": [""],
#     "fsm_graph":
# }


START_STATE_KEY = "start_state"
ACCEPT_STATES_KEY = "accept_state"
FSM_GRAPH_KEY = "fsm_graph"


def load_schema(json_fsm_path):
    ret = {START_STATE_KEY: "a", ACCEPT_STATES_KEY: ["a"], FSM_GRAPH_KEY: {"a": {}}}
    with open(json_fsm_path, "r") as json_fp:
        json.load(json_fp)
    return ret


def load_start_state(json_fsm_path):
    schema_dict = load_schema(json_fsm_path)
    return schema_dict[START_STATE_KEY]


def load_accept_states(json_fsm_path):
    schema_dict = load_schema(json_fsm_path)
    return schema_dict[START_STATE_KEY]


def load_fsm_graph(json_fsm_path):
    schema_dict = load_schema(json_fsm_path)
    return schema_dict[FSM_GRAPH_KEY]


def analyze_fsm(json_fsm_path, input_string):
    start_state = load_start_state(json_fsm_path)
    accept_states = load_accept_states(json_fsm_path)
    fsm_graph = load_fsm_graph(json_fsm_path)

    cur_state = start_state
    for n in input_string:
        if n not in fsm_graph[cur_state]:
            print(f"Missing transistion: ({cur_state}) -- {n} -> (reject)")
            return False

        next_state = fsm_graph[cur_state][int(n)]
        print(f"Transistion: ({cur_state}) -- {n} -> ({next_state})")

    return cur_state not in accept_states


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json_fsm", help="Path to FSM representing JSON", type=str, required=True)
    parser.add_argument("--input_str", help="Input string to check if accepted", type=str, required=True)
    args = parser.parse_args()

    ret = analyze_fsm(args.input_str, args.json_fsm)
    print(f"Input string accepted by graph: {ret}")
