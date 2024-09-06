## Essential Questions

- What techniques can find a solution in a complex search space?
- How should different skill levels utilize Chatbots?

## Lesson Plan

In this lesson, students are exposed to the power of ChatBots such as ChatGPT
and Claude.ai. First, we review concepts about search space exploration from the
previous class. Then, we see how Claude.ai would have answered the given
homework and critique its answers. After that, I show them what ChatGPT output
when I asked it to create a version of "Search Space Battleship" and dig
through the code it produced. Finally, we discuss all of this.

### Setup

- Connection to Claude.ai
    - **Clear our any old history** for both ChatGPT and Claude
    - Prompt for Claude.ai of the form:
```
I am trying to use Malcolm Gladwell's talk "On Spaghetti Sauce" to understand
how search spaces and search space exploration work. Could you create a medium
length paragraph answering the question "what mistake did Prego make in terms of
their objective function when trying to find the perfect spaghetti sauce"?
```
- `landscapeGame.pdf` printed out
    - Single page (two-sided) of code from `./chatbot_output`

### Actual Lesson

- Review
    - What did we do yesterday?
    - What do **parameters** mean?
    - What is an **object function** mean?
    - What is a local maxima?
    - What is max gradient ascent?
    - How does "growing flowers" map onto this?
    - How does "perfect pasta sauce" map onto this?
- Claude.ai intro
    - Look at the homework
    - We know Claude.ai is good at this kind of thing, so let's see what it says
        - Ask question on homework of Claude.ai
    - Thoughts?
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
- Took code and modified it a bit
    - Play game stored in `./chatbot_output_improved` (don't show code)
    - Play game stored in `./chatbot_output`
    - This is bonkers!
    - What does this say about programming?
- Today, as a class going to modify game to make it match my vision
    - Hand out `landscapeGame.pdf`
        - Explain what's going on
        - Emphasize how similar JavaScript is to Python
        - Ask notice/wonder questions
    - Modify game
        - Have students pair up
            - Ask how would make small changes
            - Give 2-3 minutes to deliberate per change
            - Have people explain what they think and then implement it
        - Changes
            - Less intense mountains
            - Wider view of where click
            - Max -> min
            - Win if see peak
            - Bigger Canvas
        - Bugs in Original code?
            - Unused variable `peaks`
- Discussion
    - What do these capabilities mean for novices?
    - What do these capabilities mean for experts?
   - What outside knowledge am I bringing to this process?
    - Why am I emphasizing Software Engineering in the class?
- If time: deploy to GitHub on my website
    - Talk about GitHub
    - Explain how website works
    - Drop files in
    - Push and then go to webpage
        - Add explainer and link to `my_projects.md`
        - Add HTML page to `_my_projects`
            - Combine into single HTML page

### Homework

- None

### Other possible homeworks

- Read https://www.theatlantic.com/newsletters/archive/2022/04/shania-twain-creativity-one-hit-wonder/629569/
    - Answer similar questions as the Spaghetti Sauce Search assignment
- Research "simulated annealing" and explain what its strategy would be
