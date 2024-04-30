#!/usr/bin/env python3
import random
import time

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
        possible_stops = flights[ana_location]
        next_stop = random.sample(list(possible_stops), 1)[0]
        time.sleep(1)
        print(f"Ana is getting on a plane in {ana_location}")
        time.sleep(1)
        print("🛫 Airplane sound 🛬")
        time.sleep(1)
        print(f"Ana arrived in {next_stop}")

        ana_location = next_stop


if __name__ == "__main__":
    ana_markov_sim()
