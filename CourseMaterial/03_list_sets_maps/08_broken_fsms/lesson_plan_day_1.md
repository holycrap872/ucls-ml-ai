## Essential Questions

- How can we use FSMs to represent real-life situations?
- How do we approach a complex system we didn’t write?

## Lesson Plan

### Setup

- `broken_fsm_structured.zip` and `broken_fsm_unstructured.zip` posted to Schoology
    - TODO: Broken FSM project ready for cloning
        - https://gitlab.ucls.uchicago.edu/erizzi/broken-fsm

### Actual Lesson

- Reflection
    - FSMs:
        - Do simple, quick problem
    - Where are FSMs used?
    - FSM formalizations
        - Example: Accept/reject various strings on simple FSM
        - Example: Create and FSM
- How to represent FSMs as graphs
    - Have come up with "schema"
- Today going to combine a few things at once
    - FSMs
    - Debugging
- Walk through `working_fsm.py`
    - Show schema
    - Show me running it
    - Have them create the json version for a particular FSM
- Walk through `broken_fsm.py`
    - https://gitlab.ucls.uchicago.edu/erizzi/broken-fsm
    - Explain the exercise
        - Intentionally seeded errors mimicking real-world
    - What are ways we could find the bugs
- Find the bugs!
    - What are techniques we can use to debug?
        - Linter
        - Read closely
        - Improve variable names
        - Write documentation
        - Type checker
        - Informative input
        - `print()` statements
            - Often the most useful
        - Breakpoints
        - Unit tests
    - Have them come up with techniques and order them from easiest to hardest
- Quick debugging example using breakpoints
    - see `debugging_examples.py`
- Go!
    - Split up into pairs
    - Switch who's on the keyboard every 5 minutes

#### Homework

- TIL on debugging technique of your choice
- Data Structure Wheaties 22

#### Resources

- https://www.madebyevan.com/fsm/
    - Make curved lines between states by making arrow and then pulling it up/down
- https://www.csfieldguide.org.nz/en/chapters/formal-languages/finite-state-automata/
- Graph lesson: https://mathigon.org/course/graph-theory/map-colouring
