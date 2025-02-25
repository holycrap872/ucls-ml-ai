## Essential Questions

- How do we design a complex piece of software?
- How can we use the past to predict the future?
- How can we use feedback to create a learning system?

## Lesson Plan


### Setup

- None

### Actual Lesson

- Review
    - Blackjack rules
    - Difficulties from third day
    - Concerns about finishing in time
- Essentials of design
    - Blackjack design
        - NamedTuples: `Card`, `RoundResult`
        - Data Structures: `deck: list[Card]`, `user_hand: list[Card]`, `dealer_hand: list[Card]`
        - Functions: `get_shuffled_deck()`, `get_hand_value()`
- Move code into `play_round() -> RoundResult:` function
    - Shows how slowly add features to build a piece of software
- Any questions?
- Go!

### Homework

- Finish blackjack

### Extension

- Multiple players against one dealer
- Implement `split`
- Pick deck size at beginning (so can practice counting cards)
