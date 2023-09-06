## Essential Questions

## Lesson Plan

### Setup

- Bunch of sets of legos with green "baseplate" (32x32) to stick them to
- Dividers
- Pre-created "example boards" (both 1d and 2d) to make clear what I'm talking about
    - I took pictures of the board and will show them in class
- Example board in case there's an odd number of students

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
        - Bunch of alogrithms to do this, but lets see what you come up with
    - 1 billion to 170 tillion parameters
- Rules
    - Play along one dimension
    - Board is 32 long (entire green lego baseplate)
    - Need to use between 35-40 legos
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
        - Simulated annealing
        - Hill climbing
        - Evolutionary
        - Bayesian
        - Neural Nets
- Do another example:
    - Training for a marathon
        - What is the objective function?
        - What are possible parameters?
        - What is the search space?

### Homework

```
This assignment has five parts:

1. Think of a problem where you "search" for the best solution. What is it?

2. What is the objective function?

3. What are 5 paramenters that are inputs to the objective function?

4. Describe in a few sentences what would likely be an input somewhere "near"
   the global maxima?

5. Describe in a few sentences what might be a local maxima and why it's a
   local maxima?
```

### Other possible homeworks

- Research "simulated annealing" and explain what its strategy would be

```
This assignment has three parts:

1. Watch [Malcolm Gladwell's "On Spaghetti Sauce" talk](
   https://ed.ted.com/lessons/malcolm-gladwell-on-spaghetti-sauce) up to 9m30s
   (although feel free to watch the rest... it's funny)!

2. List 5 **parameters** that can be altered to affect the taste of spaghetti sauce.

3. Write one paragraph answering the question "what mistake did Prego make in
   terms of their **objective function** when asking Howard to find the perfect
   spaghetti sauce"?
```
