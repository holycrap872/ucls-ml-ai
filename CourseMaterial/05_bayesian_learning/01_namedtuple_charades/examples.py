import typing


# Insect
class Thing1(typing.NamedTuple):
    num_eyes: int
    num_legs: int
    weight: float
    has_wings: bool


# Employee
class Thing2(typing.NamedTuple):
    id: int
    role: str
    salary: int
    years: int


# Coffee Shop
class Thing3(typing.NamedTuple):
    num_tables: int
    num_employees: int
    has_wifi: bool
    closing_time: int


# CPU
class Thing4(typing.NamedTuple):
    cores: int
    flops: int
    watts: float
    cache_size: int


# Movie Theater
class Thing5(typing.NamedTuple):
    num_screens: int
    seat_capacity: int
    has_imax: bool
    popcorn_price: float
