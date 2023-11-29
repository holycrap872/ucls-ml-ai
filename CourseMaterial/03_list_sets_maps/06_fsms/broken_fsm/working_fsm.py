#!/usr/bin/env python3
import argparse
import json

# Seeded bugs:
# 1. Swapped parameters
#    - Difficulty: easy
#    - Expected time: 3m
# 2. Missing `ret =` in `load_schema()`
#    - Difficulty: medium
#    - Expected time: 5m
# 3. Incorrect `int()` cast
#    - Difficulty: easy
#    - Expected time: 2m
# 4. Incorrectly used `START_STATE_KEY` in `load_accept_states`
#    - Difficulty: medium
#    - Expected time: 5m
# 5. Incorrectly spelled `ACCEPT_STATES_KEY` const
#    - Difficulty: easy
#    - Expected time: 1m
# 6. `cur_state = next_state` missing
#    - Difficulty: hard
#    - Expected time: 10m
# 7. `cur_state not in accept_states` -> `cur_state in accept_states`
#    - Difficulty: hard
#    - Expected time: 10m
#    - I think this one might be one step too far so I might remove it

# Schema
# {
#     "start_state": "",
#     "accept_states": [""],
#     "fsm_graph":
# }


START_STATE_KEY = "start_state"
ACCEPT_STATES_KEY = "accept_states"
FSM_GRAPH_KEY = "fsm_graph"


def load_schema(json_fsm_path: str) -> dict:
    with open(json_fsm_path, "r") as json_fp:
        return json.load(json_fp)


def load_start_state(json_fsm_path: str) -> str:
    schema_dict = load_schema(json_fsm_path)
    ret = schema_dict[START_STATE_KEY]
    assert isinstance(ret, str)
    return ret


def load_accept_states(json_fsm_path: str) -> list[str]:
    schema_dict = load_schema(json_fsm_path)
    ret = schema_dict[ACCEPT_STATES_KEY]
    assert isinstance(ret, list)
    for elem in ret:
        assert isinstance(elem, str)
    return ret


def load_fsm_graph(json_fsm_path: str) -> dict[str, dict[str, str]]:
    schema_dict = load_schema(json_fsm_path)
    ret = schema_dict[FSM_GRAPH_KEY]
    assert isinstance(ret, dict)
    return ret


def analyze_fsm(json_fsm_path: str, input_string: str) -> bool:
    start_state = load_start_state(json_fsm_path)
    accept_states = load_accept_states(json_fsm_path)
    fsm_graph = load_fsm_graph(json_fsm_path)

    assert start_state in fsm_graph
    for accept_state in accept_states:
        assert accept_state in fsm_graph

    cur_state = start_state
    for c in input_string:
        next_state = fsm_graph[cur_state][c]
        print(f"Transistioning {cur_state} -> {next_state}")
        cur_state = next_state

    return cur_state in accept_states


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json_fsm", help="Path to FSM representing JSON", type=str, required=True)
    parser.add_argument("--input_str", help="Input string to check if accepted", type=str, required=True)
    args = parser.parse_args()

    ret = analyze_fsm(args.json_fsm, args.input_str)
    print(f"Input string accepted by graph: {ret}")
