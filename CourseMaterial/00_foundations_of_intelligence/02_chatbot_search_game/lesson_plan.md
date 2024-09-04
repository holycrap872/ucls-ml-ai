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

- YouTube Videos loaded up
    - https://youtu.be/IHZwWFHWa-w?t=417
- "One Hit Wonder" assignment posted to Schoology


### Actual Lesson

- Review
    - What did we do yesterday?
    - What do **parameters** mean?
    - What is an **object function** mean?
    - What is a local maxima?
    - What is max gradient ascent?
    - How does "growing the perfect sunflower" map onto this?
- Claude.ai intro
    - Look at the homework
    - We know Claude.ai is good at this kind of thing, so let's see what it says
        - Ask question on homework of Claude.ai
- I had an idea for a game
    - Basically the same as what we did yesterday
    - I couldn't find it online
    - I asked ChatGPT:
        ```
        Could you give me some sample JavaScript code that does the following:
        1. Randomly creates a 2d landscape (with mountains and valleys)
        2. Initially covers the landscape with a black screen
        3. Where ever students click, highlights a vertical slice of where they clicked
        4. Counts how many guesses it takes for them to uncover the tallest peak
        ```
    - See `./chatbot_ouput` for what it says
- Show game
    - This is bonkers!
    - What does this say about programming?
- Explain what's going on
- Modify game
    - Ask how would make small changes and have them in pairs suggest changes
        - Emphasize how similar JavaScript is to Python
    - Changes
        - Wider view of where click
        - Less intense mountains
        - Max -> min
        - Bigger Canvas
- Discussion
    - What does this mean?
    - Why am I emphasizing Software Engineering in the class?
    - How is CS different from English?
- Explain all algorithms we're going to learn
    - Simulated annealing (don't actually code)
    - Hill climbing (don't actually code)
    - Evolutionary
    - Bayesian
    - Neural Nets
- Gradient descent (ascent) in our case
    - https://youtu.be/IHZwWFHWa-w?t=420
- Get started on homework

### Homework

- Read https://www.theatlantic.com/newsletters/archive/2022/04/shania-twain-creativity-one-hit-wonder
    - Answer similar questions as the Spaghetti Sauce Search assignment

### Other possible homeworks

- Research "simulated annealing" and explain what its strategy would be