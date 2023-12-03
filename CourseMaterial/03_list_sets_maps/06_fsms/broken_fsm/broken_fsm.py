#!/usr/bin/env python3
import argparse
import json

# Schema
# {
#     "start_state": "a",
#     "accept_states": ["b"],
#     "fsm_graph": {"a": {"1": "b", "0": "b"}}
# }


START_STATE_KEY = "start_state"
ACCEPT_STATES_KEY = "accept_state"
FSM_GRAPH_KEY = "fsm_graph"


def load_schema(json_fsm_path):
    """
    This function takes a path to a json file. It then open that file and loads
    the FSM (represented as a dictionary) from the file.

    :param json_fsm_path: Path to json dict representing FSM
    :return: Dictionary containing each part of FSM
    """
    ret = {START_STATE_KEY: "a", ACCEPT_STATES_KEY: ["a"], FSM_GRAPH_KEY: {"a": {}}}
    with open(json_fsm_path, "r") as json_fp:
        json.load(json_fp)
    return ret


def load_start_state(json_fsm_path):
    """
    This function loads the start state of a particular FSM from a json file.

    :param json_fsm_path: Path to json dict representing FSM
    :return: The start state of the FSM
    """
    schema_dict = load_schema(json_fsm_path)
    return schema_dict[STAR_STATE_KEY]


def load_accept_states(json_fsm_path):
    """
    This function loads the accept state(s) of a particular FSM from a json file.

    :param json_fsm_path: Path to json dict representing FSM
    :return: All of the accept states with the machine
    """
    schema_dict = load_schema(json_fsm_path)
    return schema_dict[ACCEPT_STATES_KEY]


def load_fsm_graph(json_fsm_path):
    """
    This function the dictionary representing the graph (nodes, and edges) of
    a particular FSM from a json file.

    :param json_fsm_path: Path to json dict representing FSM
    :return: The dictionary representing the graph of the FSM
    """
    schema_dict = load_schema(json_fsm_path)
    return schema_dict[FSM_GRAPH_KEY]


def analyze_fsm(json_fsm_path, input_string):
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
    start_state = load_accept_states(json_fsm_path)
    accept_states = load_accept_states(json_fsm_path)
    fsm_graph = load_fsm_graph(json_fsm_path)

    cur_state = start_state
    for n in input_string:
        if n not in fsm_graph[cur_state]:
            print(f"Missing transistion: ({cur_state}) -- {n} -> (reject)")
            return False

        next_state = fsm_graph[cur_state][int(n)]
        print(f"Transistion: ({cur_state}) -- {n} -> ({next_state})")

    return accept_states


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json_fsm", help="Path to FSM representing JSON", type=str, required=True)
    parser.add_argument("--input_str", help="Input string to check if accepted", type=str, required=True)
    args = parser.parse_args()

    ret = analyze_fsm(args.inpu_str, args.json_fsm)
    print(f"Input string accepted by graph: {bool(ret)}")
