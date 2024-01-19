## Essential Questions

- How can we use the past to predict the future?
- How can we use feedback to create a learning system?

## Lesson Plan

The point of this lesson is to have the students build on/alter the blackjack
game they created in previously lessons. This has two effects. First, it forces
them to revisit their own code and understand the importance of making it
readable/understandable for themselves. Second it allows us to replace a "human
agent" with a "bayesian" agent that gradually learns to play blackjack.

During the lesson(s), we compare our bot with the "ideal" solved version of
casino blackjack and run various simulations for rule changes.

### Setup

None

### Actual Lesson

- Review
    - Bayes theorem
    - 3Blue1Brown
- Watch https://www.youtube.com/watch?v=Zxm4Xxvzohk
    - Discuss how tree relates to bayes theorem
    - Whether to think of it as a Venn Diagram or a Tree
- Bayesian data
    - Use sample blackjack data to answer a bunch of questions
        - P(Win)
        - P(Win | p16)
        - P(Win | Stay)
        - P(Win | p16, d10)
        - P(Win | p16, d10, Hit)
        - P(Win | p16, d10, Stay)
    - Why is this useful?
- Today we're basically going to do same thing as "rule bot"
    - Instead of a "rule bot" playing, we're going to have a "bayesian bot"
- Bayesian Bot description:
    - Use the data I give you to make decisions
    - Play 1000 games and find win %
- Advanced: create a "learning bayesian bot"
    - It should do "the easy stuff" automatically
        - e.g., it should always hit when less than 20
        - Only need to make a decision when greater than 11
    - Self-teaching
    - Play 100000 games
        - Graph win percentage in chunks of 1000
- Exploration:
    - What is the win percentage if the dealer sticks on 16 or greater, or 19 or greater?
    - Create graph showing % chance of winning under particular situations
        - e.g., Dealer showing a 9

#### Extensions

- Amount to bet (expected value)
- How do things change w/ dealing from 1 deck vs 6 decks?

### Resources

- https://towardsdatascience.com/winning-blackjack-using-machine-learning-681d924f197c
