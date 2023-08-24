#!/usr/bin/env python3
import argparse
import random
import string
import typing


def mutate(name: str) -> str:
    new_name = ""
    for c in name:
        choice = random.randint(0, 20)

        if choice == 0:
            new_name += c
            new_name += c
        elif choice == 1:
            continue
        elif choice == 2:
            new_name += random.choice(string.ascii_letters)
        elif choice == 3:
            new_name += random.choice(name)
        else:
            new_name += c

    return new_name


def get_fitness(name: str, end_name: str) -> int:
    if len(name) > len(end_name):
        longest = name
        shortest = end_name
    else:
        longest = end_name
        shortest = name

    diff = 0
    for i in range(0, len(longest)):
        if i >= len(shortest):
            diff += 255

        else:
            diff += abs(ord(longest[i]) - ord(shortest[i]))
    return diff


def create_mutant_set(names: typing.List[str], max_mutants: int) -> typing.List[str]:
    ret_list: typing.List[str] = []
    while len(ret_list) < max_mutants:
        name_to_mutate = random.choice(names)
        ret_list.append(mutate(name_to_mutate))

    return ret_list


def run(start_name: str, end_name: str) -> None:
    mutant_list = [start_name]
    while True:
        mutant_list = create_mutant_set(mutant_list, 50)
        print(mutant_list)

        fitness = [(name, get_fitness(name, end_name)) for name in mutant_list]
        fitness.sort(key=lambda e: e[1])
        fitness = fitness[0: 3]
        print(fitness)

        mutant_list = [n[0] for n in fitness]
        if mutant_list[0] == end_name:
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", help="Starting Name", type=str, required=True)
    parser.add_argument("-e", help="Ending Name", type=str, required=True)
    args = parser.parse_args()

    run(args.s, args.e)
