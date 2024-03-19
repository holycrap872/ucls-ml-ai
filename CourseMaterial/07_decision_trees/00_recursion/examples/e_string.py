#!/usr/bin/env python3
def es_in_string(s: str) -> int:
    if len(s) == 0:
        breakpoint()
        return 0
    else:
        first = s[0]
        rest = s[1:]
        if first == "e":
            return 1 + es_in_string(rest)
        else:
            return es_in_string(rest)


print(es_in_string("elephant"))
