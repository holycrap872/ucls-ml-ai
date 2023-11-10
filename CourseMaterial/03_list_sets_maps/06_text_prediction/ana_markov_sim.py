#!/usr/bin/env python3
import random

AVERAGEMONT = "AVERAGEMONT"
DISCRETOWN = "DISCRETOWN"
CONTINUOPOLIS = "CONTINUOPOLIS"
BAYESVILLE = "BAYESVILLE"
EAST_VANDERMONDE = "EAST_VANDERMONDE"


def ana_markov_sim() -> None:
    flights: dict[str, set[str]] = {
        AVERAGEMONT: {DISCRETOWN, BAYESVILLE, CONTINUOPOLIS},
        DISCRETOWN: {AVERAGEMONT, BAYESVILLE},
        CONTINUOPOLIS: {AVERAGEMONT, BAYESVILLE},
        BAYESVILLE: {AVERAGEMONT, DISCRETOWN, CONTINUOPOLIS, EAST_VANDERMONDE},
        EAST_VANDERMONDE: {BAYESVILLE},
    }

    ana_location = BAYESVILLE
    for _ in range(0, 5):
        next_stop = random.sample(flights[ana_location], 1)[0]
        print(f"Ana is getting on a plan in {ana_location}")
        print("Airplane sound")
        print(f"Ana arrived in {next_stop}")


if __name__ == "__main__":
    ana_markov_sim()
