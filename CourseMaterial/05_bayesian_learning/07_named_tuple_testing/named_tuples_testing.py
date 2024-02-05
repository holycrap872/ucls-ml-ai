#!/usr/bin/env python3
import typing


class Person(typing.NamedTuple):
    name: str
    age: int


class Course(typing.NamedTuple):
    code: str
    students_enrolled: int
    max_students: int


class Appointment(typing.NamedTuple):
    start_time: int
    end_time: int


class Vehicle(typing.NamedTuple):
    make: str
    color: str
    vin: int
    is_electric: bool


class Location(typing.NamedTuple):
    name: str
    latitude: float
    longitude: float


def name_me_0(person: Person) -> bool:
    assert len(person.name) > 0

    first_letter = person.name[0]
    return first_letter.lower() in "aeiou"


def name_me_1(people: list[Person]) -> bool:
    assert len(people) > 1

    seen = set()
    for person in people:
        if person.name in seen:
            return True
        else:
            seen.add(person.name)

    return False


def name_me_2(courses: list[Course], course_code: str) -> bool:
    assert len(courses) > 1

    for course in courses:
        if course.code == course_code:
            return course.students_enrolled >= course.max_students

    return False


def name_me_3(appointments: list[Appointment]) -> bool:
    sorted_appointments = sorted(appointments, key=lambda x: x.start_time)
    for i in range(1, len(sorted_appointments)):
        if sorted_appointments[i].start_time < sorted_appointments[i - 1].end_time:
            return True
    return False


def name_me_4(cars: list[Vehicle]) -> bool:
    assert len(cars) > 2

    expected_sequence = None
    for car in cars:
        if expected_sequence is None:
            expected_sequence = car.vin
        elif car.vin != expected_sequence:
            return False

        expected_sequence += 1

    return True


def name_me_5(cars: set[Vehicle]) -> bool:
    assert len(cars) > 1

    count = sum(car.is_electric for car in cars)
    return count * 2 == len(cars)


def name_me_6(location: Location) -> bool:
    if not (-90 <= location.latitude <= 90) or not (-180 <= location.longitude <= 180):
        return False

    return True


def name_me_7(locations: dict[Person, Location]) -> bool:
    assert len(locations) >= 2

    seen_locations = set()
    for location in locations.values():
        if location in seen_locations:
            return True
        seen_locations.add(location)
    return False
