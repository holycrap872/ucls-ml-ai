## Essential Questions

- How can we use the past to predict the future?
- How can we use feedback to create a learning system?

## Lesson Plan

The point of this lesson is to have the students start to modify their code
in preparation for dropping in a "bayesian learning system". In this case, they
replace the user with a simple rule bot (learning about interfaces in the
process) and then graph which value is the "best" value to stand on.

### Setup

- One deck of cards for every two students

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
    - Making something easy to "swap out" implies the use of interfaces
- Interfaces
    - Definition: A shared boundary across which two or more separate components of a computer system exchange information
    - Real life examples:
        - Wall sockets
        - Ask class to come up with one
    - Programming languages:
        - Java: whole formalization behind it
        - Python: Basically just make sure functions have the same "shape"
            - show `socket_interface_example.py`
            - show `operation_interface_example.py`
- Today we're basically going to do same thing
    - Instead of a new person playing, we're going to have a "rule bot"
    - How is this like an interface?
        - Talk through someone's blackjack code
- Goals for today:
    - Replace user with “rule bots”
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

#### Homework

- Finish assignment
- Prepare for bayesian statistics
    - If don't know probability trees, watch:
        - Independent:
            - https://www.youtube.com/watch?v=mkDzmI7YOx0
        - Dependent:
            - https://www.youtube.com/watch?v=NOOMC_rc-8Q
    - Complete probability worksheet

#### Extension

- Create more complex "rule bot" or your own
- Compare more complex rule bot to other, existing bots
