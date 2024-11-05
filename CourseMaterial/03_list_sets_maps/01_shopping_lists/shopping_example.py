#!/usr/bin/python3


def list_grocery_list() -> None:
    gl = ["apple", "pear", "ice cream"]
    gl.append("bacon")
    gl.append("bacon")
    gl.pop(0)
    print("Third item in list: ", gl[3])
    print("Pear?: ", "pear" in gl)

    for item in gl:
        print(item)

    print("List grocery list:", gl)


def set_grocery_list() -> None:
    gs = {"apple", "pear", "ice cream"}
    gs.add("bacon")
    gs.add("bacon")
    gs.remove("apple")

    print("Pear?: ", "pear" in gs)

    for item in gs:
        print(item)

    print("List grocery list:", gs)


def dict_grocery_list() -> None:
    gd = {"apple": 4, "pear": 3, "ice cream": 20}
    gd["bacon"] = 2
    gd["ice cream"] = 2
    gd.pop("ice cream")
    print(gd["bacon"])

    print("Pear?: ", "pear" in gd)
    print("Pear?: ", 20 in gd)

    for key in gd:
        print(key, gd[key])


if __name__ == "__main__":
    # list_grocery_list()
    set_grocery_list()
    # dict_grocery_list()
