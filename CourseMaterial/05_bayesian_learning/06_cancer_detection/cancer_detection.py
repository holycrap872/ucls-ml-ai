#!/usr/bin/env python3
import typing


class CancerData(typing.NamedTuple):
    sample_num: str
    smoothness: int
    area: int
    radius: int
    is_cancer: bool


def parse_data(path: str) -> list[CancerData]:
    ret = []
    with open(path) as fp:
        s = fp.read().split("\n")[1:]
        for row in s:
            d = row.split(",")
            cd = CancerData(
                sample_num=d[0],
                smoothness=int(d[1]),
                area=int(d[2]),
                radius=int(d[3]),
                is_cancer="mal" in d[-1],
            )

            ret.append(cd)

    return ret


def find_matches(data: list[CancerData], smoothness: int, area: int, radius: int) -> tuple[int, int]:
    mal = 0
    ben = 0
    for d in data:
        if d.smoothness == smoothness and d.area == area and d.radius == radius:
            if d.is_cancer:
                mal += 1
            else:
                ben += 1

    return mal, ben


if __name__ == "__main__":
    training_list = parse_data("CourseMaterial/05_bayesian_learning/06_cancer_detection/cancer.csv")
    print(len(training_list))
    test_list = parse_data("CourseMaterial/05_bayesian_learning/06_cancer_detection/cancer_test.csv")
    print(len(test_list))

    correct = 0
    wrong = 0
    for test in test_list:
        mal, ben = find_matches(training_list, test.smoothness, test.area, test.radius)

        cancer = mal > ben
        if cancer == test.is_cancer:
            correct += 1
        else:
            wrong += 1

    print(correct, wrong)
