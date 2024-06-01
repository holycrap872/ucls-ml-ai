## Essential Questions

- What are FSMs and where are they useful?

## Lesson Plan

### Setup

- Broken FSM project ready for cloning
    - https://gitlab.ucls.uchicago.edu/erizzi/broken-fsm

### Actual Lesson

- Reflection
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
        - Type checker
        - Good test cases
        - `print()` statements
            - Often the most useful
        - Guarded breakpoints
        - Unit tests
    - Have them come up with techniques and order them from easiest to hardest
- Quick debugging example using breakpoints
    - see `debugging_examples.py`
- `git clone` from gitlab
    - Make clear what types of fixes required
        - One addition of `_ = _`
        - One addition of `_ in _`
    - Go!

#### Homework

- Finish debugging and get program working
- Data structures problem set

#### Resources

- https://www.madebyevan.com/fsm/
    - Make curved lines between states by making arrow and then pulling it up/down
- https://www.csfieldguide.org.nz/en/chapters/formal-languages/finite-state-automata/
- Graph lesson: https://mathigon.org/course/graph-theory/map-colouring
