## Essential Questions

- What is a search space?
- What techniques can find a solution in a large search space?

## Lesson Plan

In this kickoff lesson, students are exposed to the concept of "search space".
First they learn the requisite vocabulary and then they start to apply it to
common problems (like baking a cake or running a race). Finally, we start to
talk about "search techniques" by playing Search Space Battleship and discuss
what they learned.

This lesson and the one that follows on the Turing Test form the basis of the
class: technical mixed with philosophical.

### Setup

- Search Space Battleship pieces
    - Bunch of sets of LEGOs with green "baseplate" (32x32) to stick them to
    - Dividers
    - Pre-created "example boards" (both 1d and 2d) to make clear what I'm talking about
        - I took pictures of the board and will show them in class
    - Example board in case there's an odd number of students
- YouTube Videos loaded up
    - https://youtu.be/IHZwWFHWa-w?t=417
- "Spaghetti Sauce Search" assignment posted to Schoology
    - https://docs.google.com/document/d/13f8gNtaOgFA_MCKX1965QIzF8IzqR16F4kFNBemDca0

### Actual Lesson

- Today going to play a game called "Search Space Battle Ship"
    - Who's played Battle Ship?
    - Explain Battle Ship
        - 2 dimensions
    - What are good strategies in Battle Ship?
        - Link each thing they say to key terms for the day
- Most of ML/AI is trying to find the best possible solution for a problem
    - Put up key words on the board and define them
        - Search Space
        - Objective Function
        - Parameters
        - Global Maxima
        - Local Maxima
    - What would "baking the perfect cake" look like?
        - What is the **objective function**?
        - What are some **parameters**?
        - Estimate of total number of parameters?
    - AL/ML is looking for a "global maxima"
        - Search "3d search space" in google for examples
        - Don't want to get stuck in a "local maxima"
        - Bunch of algorithms to do this, but lets see what you come up with
    - Size of "real problems": 1 billion to 170 trillion parameters
- Rules
    - Play along one dimension
    - Board is 32 long (entire green LEGO baseplate)
    - Need to use between 35-40 LEGOs
    - Must have a global maxima between 4 and 7
    - Must have between 2 and 4 local maximas
    - Maximum slope of 1
    - Each get 12 guesses. At the end you guess the other person's global max
- Show them my example boards and ask what's good/bad about them
- Let play and debrief
    - What were people's strategies?
    - What was the hardest solution to find?
- Reset and replay against a new partner
- Let play and debrief
    - How many **parameters** in each game?
    - Gradient descent (ascent) in our case
        - https://youtu.be/IHZwWFHWa-w?t=420
    - Explain all algorithms we're going to learn
        - Simulated annealing (don't actually code)
        - Hill climbing (don't actually code)
        - Evolutionary
        - Bayesian
        - Neural Nets
- Do another example:
    - Training for a marathon
        - What is the objective function?
        - What are possible parameters?
        - What is the search space?

### Homework

- `Spaghetti Sauce Search`

### Other possible homeworks

- Read https://www.theatlantic.com/newsletters/archive/2022/04/shania-twain-creativity-one-hit-wonder
    - Answer the same questions as the Spaghetti Sauce talk
- Research "simulated annealing" and explain what its strategy would be
- Come up with own "search space"
    ```
    This assignment has five parts:

    1. Think of a problem where you "search" for the best solution. What is it?

    2. What is the objective function?

    3. What are 5 parameters that are inputs to the objective function?

    4. Describe in a few sentences what would likely be an input somewhere "near"
    the global maxima?

    5. Describe in a few sentences what might be a local maxima and why it's a
    local maxima?
    ```