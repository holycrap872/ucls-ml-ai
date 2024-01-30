## Essential Questions

- What is the best way to store related data?
- What is the difference between dictionaries and objects?

## Lesson Plan

### Setup

None

### Actual Lesson

- Review
    - Debugging techniques
    - What was easy/hard
    - Design of system
    - Point of interface
    - How could be easily plugged in as blackjack bot
- Code review
    - Volunteer
    - What went well
    - What went poorly
- Goal today
    - New concept called "NamedTuples"
    - Refactor code so uses NamedTuples and easier to understand
- NamedTuples
    - Bundled data
    - Typed so easier to debug
        - No "key" access errors
        - Know type of values
    - Compare with objects
        - Basically the same thing without "methods"
            - Can add methods
    - Compare with dicts
        - All Python stuff is dictionaries at the bottom
        - Difficult to work with
        - Dictionaries are for variable sized data (graphs)
- Goals
    - Replace dicts with NamedTuples in suggester
    - Update functions to use NamedTuples
    - Tests

#### Homework

- Finish refactor/tests
