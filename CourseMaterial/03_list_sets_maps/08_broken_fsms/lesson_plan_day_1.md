## Essential Questions

- How can we use FSMs to represent real-life situations?
- How do we approach a complex system we didn’t write?

## Lesson Plan

In this lesson, students are asked to use their theoretical understanding of
Finite State Machines to debug and fix a broken software representation of them.
The point of the lesson is two-fold:
1. Acknowledge that at least half the students would struggle to write the FSM
   software from scratch.
2. Allow students to use debugging skills to marry their theoretical
   understanding with real practice.
As such, students talk through different debugging techniques and then use them
to try and get the program running.

> Note: one complaint from students is this lesson was "too fast", so be sure
  to take time and show them what a working version of the software should do.

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
    - Talk through the output and what is going on
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
    - Split up **into pairs**
    - Switch who's on the keyboard every 5 minutes

### Homework

- TIL on debugging technique of your choice
- Data Structure Wheaties 22

### Resources

- https://www.madebyevan.com/fsm/
    - Make curved lines between states by making arrow and then pulling it up/down
- https://www.csfieldguide.org.nz/en/chapters/formal-languages/finite-state-automata/
- Graph lesson: https://mathigon.org/course/graph-theory/map-colouring
