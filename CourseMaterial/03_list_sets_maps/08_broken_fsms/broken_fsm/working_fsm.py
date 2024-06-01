#!/usr/bin/env python3
import argparse
import json

# Seeded bugs:
# 0. Misspelled `START_STATE_KET`
#    - Difficulty: trivial
#    - Expected time: 1m
# 1. Misspelled `args.input_str`
#    - Difficulty: easy
#    - Expected time: 2m
# 2. Swapped parameters
#    - Difficulty: easy
#    - Expected time: 3m
# 3. Incorrect `int()` cast
#    - Difficulty: easy
#    - Expected time: 2m
# 4. Incorrect `start_state = load_accept_states(...)`
#    - Difficulty: medium (caught with typing)
#    - Expected time: 5m
# 5. Missing `ret =` in `load_schema()`
#    - Difficulty: hard
#    - Expected time: 7m
# 6. Incorrectly spelled `ACCEPT_STATES_KEY` const
#    - Difficulty: easy
#    - Expected time: 1m
# 7. `cur_state = next_state` missing
#    - Difficulty: hard
#    - Expected time: 10m
# 8. `return accept_states` -> `return cur_state in accept_states`
#    - Difficulty: medium
#    - Expected time: 5m

# Schema
# {
#     "start_state": "a",
#     "accept_states": ["b"],
#     "fsm_graph": {"a": {"1": "b", "0": "b"}}
# }


START_STATE_KEY = "start_state"
ACCEPT_STATES_KEY = "accept_states"
FSM_GRAPH_KEY = "fsm_graph"


def load_schema(json_fsm_path: str) -> dict:
    """
    This function takes a path to a json file. It then open that file and loads
    the FSM (represented as a dictionary) from the file.

    :param json_fsm_path: Path to json dict representing FSM
    :return: Dictionary containing each part of FSM
    """
    with open(json_fsm_path, "r") as json_fp:
        return json.load(json_fp)


def load_start_state(json_fsm_path: str) -> str:
    """
    This function loads the start state of a particular FSM from a json file.

    :param json_fsm_path: Path to json dict representing FSM
    :return: The start state of the FSM
    """
    schema_dict = load_schema(json_fsm_path)
    ret = schema_dict[START_STATE_KEY]
    assert isinstance(ret, str)
    return ret


def load_accept_states(json_fsm_path: str) -> list[str]:
    """
    This function loads the accept state(s) of a particular FSM from a json file.

    :param json_fsm_path: Path to json dict representing FSM
    :return: All of the accept states with the machine
    """
    schema_dict = load_schema(json_fsm_path)
    ret = schema_dict[ACCEPT_STATES_KEY]
    assert isinstance(ret, list)
    for elem in ret:
        assert isinstance(elem, str)
    return ret


def load_fsm_graph(json_fsm_path: str) -> dict[str, dict[str, str]]:
    """
    This function the dictionary representing the graph (nodes, and edges) of
    a particular FSM from a json file.

    :param json_fsm_path: Path to json dict representing FSM
    :return: The dictionary representing the graph of the FSM
    """
    schema_dict = load_schema(json_fsm_path)
    ret = schema_dict[FSM_GRAPH_KEY]
    assert isinstance(ret, dict)
    return ret


def analyze_fsm(json_fsm_path: str, input_string: str) -> bool:
    """
    The main logic function that determines whether a given input string is
    accepted/rejected by a particular FSM. It works by starting at the start
    state and transistioning through the machine until the given input string
    is exhausted. It then returns whether the machine ended in an accept state
    or not.

    :param json_fsm_path: Path to json dict representing FSM
    :param input_string: The string to test whether the FSM accepts/rejects it
    :return: True/False about whether the input string is accepted/rejected
    """
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
    print(f"Input string accepted by graph: {bool(ret)}")
