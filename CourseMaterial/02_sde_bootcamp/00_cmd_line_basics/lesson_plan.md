## Essential Questions

- How can we use the command-line to increase our effectiveness?
- How much effort should I put into understanding the tools I'm using?

## Lesson Plan

In this class, we will discuss how powerful (and confusing) the command-line
is and how it will pop up over and over again throughout the course. After the
discussion/lecture, students will play "GameShell" to reinforce the concepts.
Note that only enough information to get through "GameShell" is given to the
students. Things like absolute/relative paths are avoided for debrief the
following day.

### Setup

- `GameShell` set up
    - https://github.com/phyver/GameShell Docker image built and pushed to computers
        - Enough docker images up and running
        ```
        docker pull erizzi/gameshell_tutorial
        docker run -it erizzi/gameshell_tutorial
        ```
- An example folder on my desktop
    - `terminal_example.zip`

### Actual Lesson

- Refresher
    - What are some signals of intelligence?
    - What is machine learning?
    - What are the themes of the class?
- Kicking off multi-week "boot camp" to get everyone up to speed
    - Based on knowledge required to be a good intern at AWS
    - Going to keep doing Python problem sets so skills don't atrophy
- Today going to learn command-line
    - Who has used the command-line before?
    - What can you do?
    - How is it different from a GUI
        - Why better than a GUI? Why worse?
- Open up command-line and do some examples
    - Where to find terminal for various systems
        - Mac is easy since based off Unix
        - Windows is harder... you might have to move to in-lab computer
    - Explore directory structure of computer
        - Do it on Desktop so you can see the changes
        - `ls`/`cd`/`mkdir`/`pwd`
        - Draw file structure on board and explain going up/down
        - **DO NOT** talk about absolute vs. relative
    - Hidden folders
- Quick review of important commands
- Introduce `GameShell`
    - Importance of `gsh check` and `gsh goal`
    - Do first goal together
- Find lab computer to work on
    - Work in pairs
    - Switch every time complete "mission"
- Go!

### Homework

- Schoology Assessment
    - What does `ls`/`mv`/`cp`/`cd` do?
    - What are the parts of a command?
    - What are the strengths/weakness of the command-line?
    - Hidden folders/files

## Resources / Random ideas

- https://www.codecademy.com/courses/learn-the-command-line/lessons/navigation
- http://web.mit.edu/mprat/Public/web/Terminus/Web/main.html
