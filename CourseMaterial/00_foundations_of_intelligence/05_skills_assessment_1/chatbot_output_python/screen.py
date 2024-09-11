import typing


class Context:
    def __init__(self):
        self.width = 100
        self.height = 100

    def clear_rect(self, x, y, width, height):
        pass

    def begin_path(self):
        pass

    def move_to(self, width, height):
        pass

    def line_to(self, x, y):
        pass

    def stroke(self):
        pass


class Click(typing.NamedTuple):
    offset_x: int


def get_click_location():
    return Click(5)
