## Essential Questions

- How do we design a complex piece of software?
- How can we use the past to predict the future?
- How can we use feedback to create a learning system?

## Lesson Plan

The point of this lesson is to have the students start to program larger systems
beyond the worksheets/lessons I've been giving them up to this point. This will
allow them to start to learn how to decompose problems. In particular, the fact
that it is blackjack allows them to build a system based on rules they
understanding without having to constantly check in with me.

### Setup

- One deck of cards for every two students
- `blackjack_simple.py` ready to play
- `Basic Blackjack Worksheet` posted to Schoology
    - https://docs.google.com/document/d/1zMJGWE1mib6mlxPPGOQxzkShuyrXd21VVt3MphwzBjE

### Actual Lesson

- Review
    - Bayesian statistics
    - NamedTuple charades
    - Homework from the previous night
- Bayesian Blackjack
    - Program that we will alter over the course of the unit
    - Initially, the user will play the game
    - Then, plug in bots to play the game
- Explain blackjack
    - Dealer is deterministic (must hit if <= 16)
    - Only see one of dealer's cards
- Have play against each other a few times so understand the rules
    - Stress that dealer has no autonomy
    - ~10m of playing
- Now going to create this game
    - Command line version to begin with: asks user if hit/stand
    - Record win %
    - After, going to replace user with bot, so much sure user decision's are function
- Design discussion:
    - What are useful functions?
    - What are return types?
    - Highlight the `get_user_decision()` function should basically be interface
- MUST CREATES:
    - `def create_deck() -> list[Card]:`
    - `def calculate_value(..., ...) -> int`
    - `def player_turn(..., ...) -> int`
        - Avoids weirdness
- Get started
    - Have two other class periods to work on it
    - Encourage you to use ChatBots since probably too ambitious w/o them

### Homework

- Grab Bag Wheaties 6 - 8
