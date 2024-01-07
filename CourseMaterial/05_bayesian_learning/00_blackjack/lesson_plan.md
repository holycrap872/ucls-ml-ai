## Essential Questions

- How can we use the past to predict the future?
- How can we use feedback to create a learning system?

## Lesson Plan

The point of this lesson is to have the students start to program larger systems
beyond the pointed worksheets/lessons I've been giving them up to this point.
This will allow them to start to decompose problems better.

The fact that it is blackjack game allows for them to build a system them mostly
know without having to constantly check in with me.

### Setup

- One deck of cards for every two students

### Actual Lesson

- Review
    - Wrap up the "learning machines" lesson
    - Any last thoughts?
- Starting a new unit: Bayesian Learning
    - It's been a long time since programmed, so first create blackjack
    - Program that we will alter over the course of the unit
    - Initially, the user will play the game
    - Then, plug in bots to play the game
- Explain blackjack
    - Dealer is deterministic (must hit if <= 16)
    - Only see one of dealer's cards
- Have play against each other a few times so understand the rules
- Now going to create this game
    - Command line version to begin with: asks user if hit/stand
    - Record win %
    - After, going to replace user with bot, so much sure user decision's are function
- Design discussion:
    - What are useful functions?
    - What are return types?
    - Highlight the `get_user_decision()` function should basically be interface
- Get started
    - Have one other class period to work on it
    - Encourage you to use ChatBots since probably too ambitious w/o them

#### Homework

- Work on blackjack
- Come in ready to talk about at least one query you made

#### Extension

- Multiple players against one dealer
- Implement `split`
- Pick deck size at beginning (so can practice counting cards)
