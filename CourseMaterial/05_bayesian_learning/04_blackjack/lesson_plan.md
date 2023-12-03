The point of this lesson is to have the students start to program larger systems
beyond the pointed worksheets/lessons I've been giving them up to this point.
This will allow them to start to decompose problems better.

The fact that it is blackjack game allows for them to build a system them mostly
know without having to constantly check in with me.

Possible extension questions:
- Amount to bet (expected value)
- How do things change w/ dealing from 1 deck vs 6 decks?

Implementation steps:
- Create a black jack game that you can play from the command line
- Create a "rule bot" that is like the dealer in that it hits up until it reaches a certain value
    - Play 1000 games and graph the win percentage of the rule bot at each value
- Use the json data I give you to create a bot
- Create bayesian bot of your own
    - It should do "the easy stuff" automatically
        - e.g., it should always hit when less than 20
        - Only need to make a decision when greater than 11
    - Play 1000 games to learn
    - Play 100000 games
        - Graph win percentage in chunks of 1000
- The rule in black jack is dealer sticks on 17 or greater.
    - What is the win percentage if the dealer sticks on 16 or greater, or 19 or greater?

### Resources

- https://towardsdatascience.com/winning-blackjack-using-machine-learning-681d924f197c
