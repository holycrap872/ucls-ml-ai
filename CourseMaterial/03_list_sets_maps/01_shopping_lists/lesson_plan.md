## Essential Questions

- What situations can different data structures model?
- How do we interact with different data "built in" data structures?

## Lesson Plan

### Setup

- `Data Structure Usage` Schoology Assessment posted
- `data_structures_cheat_sheet.docx` printed out
- `shopping_example.py` open and ready to go

### Actual Lesson

- Reflection
    - What is a data structure?
        - container
    - Maps, sets, lists
    - Discuss worksheet
        - Presidents of the United States
        - Keywords in a book
        - "In da club" vs. "waiting to get in da club"
- Power of dictionaries:
    - Dictionaries as objects
    - Do people as dictionaries
        - `eric = {"profession": "teacher", "location": "chicago"}`
    - Stress that's why they're so powerful
- Encode a shopping list as list, set, map
    - Hand out cheat sheet -> Have them fill out as they go
    - Do each container (see `list_set_map_ex.py`):
        - List
            - `append`
            - `pop(index)`
            - `in`
            - `for _ in _`
        - Set
            - `add`
            - `remove(item)`
            - `in`
            - `for _ in _`
        - Dict
            - `[]`
            - `.pop(key)`
            - `in`
            - `for _ in _`
            - `for _ in _.items()`
- What do you see/notice about this?
    - All containers are accessed pretty similarly
- Do problems together as if part of data structure wheaties:
    - Go to in git and make sure nothing is there
    - Find smallest key **without sort()**
    - Function that takes a list of integers and returns a "count dict"
        - Counting is incredibly common
        - Do words in a sentence together
- Get started on homework

### Homework

- Schoology Assessment
- TIL entry about five methods of the `dict` data structure

### Possible Extensions

- Go through ridiculous shopping example I made (see README.md)
