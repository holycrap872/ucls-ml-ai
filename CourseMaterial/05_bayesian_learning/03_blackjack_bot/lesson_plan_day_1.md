## Essential Questions

- How can we use the past to predict the future?
- How can we use feedback to create a learning system?

## Lesson Plan

The point of this lesson is to have the students start to modify their code
in preparation for dropping in a "bayesian learning system". In this case, they
replace the user with a simple rule bot (learning about interfaces in the
process) and then graph which value is the "best" value to stand on.

### Setup

- `Blackjack Bot Worksheet` loaded up in Schoology
    - https://docs.google.com/document/d/1lurIZi_SWNf56cJHxNf0FcXbpbzKZZOucENvi6wU1JQ

### Actual Lesson

- Review
    - What was easy/hard?
    - How did ChatBots help/hurt with our design?
- Code review
    - Pick someone's code
    - Walk through and discuss
    - What is your totally your code and what was inspired by ChatBot?
- Today going to make some changes to program
    - Going to "swap out" out the user's decisions
    - Called refactoring
        - Refactoring is incredibly common
        - Add a feature and keep going
        - Measure of software engineer is how well your code can adapt
    - Good refactoring puts stuff into functions
        - Easy to then reorder and create stuff
- Today we're basically going to do same thing
    - Instead of a new person playing, we're going to have a "rule bot"
- Goals for today:
    - Replace user with "rule bots"
    - Rule bots:
        - Always hit when below a certain number
        - Always stay when above or equal to a certain number
    - Run 1000 games for 12 different rule bots (stand on 10 - 21)
    - Capture win % for each rule bot
    - Create a bar graph for the win % using `matplotlib`
- Discuss goals:
    - Hint: Use a loop
    - Hint: Only need one rule bot that takes a given value
    - Hint: Functions are your friend
- Go!
- Reflection
    - Where ever commenting out chucks of code -> function

### Homework

- None