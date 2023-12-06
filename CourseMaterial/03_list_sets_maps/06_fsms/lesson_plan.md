## Essential Questions

- What are FSMs and where are they useful?

## Lesson Plan

### Setup

- Manufactoria on computers in lab
- `fsm_worksheet.docx` printed out
- `broken_fsm.py` loaded up in Schoology

### Actual Lesson

#### Day 1

- Reflection
- Manufactoria
    - Walk through rules
    - Hint at FSMs being behind the scenes
- Play!
    - Play in pairs
    - Pair programming theater?
- Last 10 minutes before leave
    - Show super simple FSM
    - Show levels
        - Stage: 2, Level: Candidate Picker
        - Stage: 3, Level: Home delivery
    - Formalize together
        - Start state
        - Graph
        - Transistions
        - Accept state

##### Homework

- Data structures problem set
- TIL entry

#### Day 2

- Reflection
    - What are FSMs
    - Where are FSMs
        - Turnstiles: http://csunplugged.mines.edu/Activities/FSA/FSA.pdf
        - Automatic doors
    - Do example FSM together
        - Only accepts 101
        - Accepts anything that starts with 11
    - Create example FSM together
        - Rejects anything that starts with 11
        - Accepts anything that ends wtih 11
- Break into pairs:
    - Do `fsm_worksheet.docx`

##### Homework

- Finish worksheet (with partner?)
- Data structures problem set

#### Day 3

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
    - Explain the exercise
        - Intentionally seeded errors mimicing real-world
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
- Download from schoology
    - Make clear what types of fixes required
        - One addition of `_ = _`
        - One addition of `_ in _`
    - Go!

##### Homework

- Finish debugging and get program working
- Data structures problem set

### Resources

- https://www.madebyevan.com/fsm/
    - Make curved lines between states by making arrow and then pulling it up/down
- If someone misses
    - https://www.youtube.com/watch?v=4rNYAvsSkwk
    - Do problems 1-5 of worksheet
