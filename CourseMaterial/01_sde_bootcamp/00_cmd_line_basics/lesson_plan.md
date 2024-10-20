## Essential Questions

- What are some basic things you can do on the command-line?
- What can the command-line do that a regular GUI cannot?

## Lesson Plan

In this class, we will discuss how powerful (and confusing) the command-line
is and how it will pop up over and over again throughout the course. After the
discussion/lecture, students will play "GameShell" to reinforce the concepts.
Note that only enough information to get through "GameShell" is given to the
students. Things like absolute/relative paths are avoided for debrief the
following day.

> Note: The GameShell game, while interesting, is too confusing on missions
  three and six to allow students to just do it by themselves. Make sure to
  bring the class together and discuss at these pain points.

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

- Review homework
    - What is the command-line?
    - What can you do with it?
    - Who has used it before?
    - How is it different from a GUI
        - Why better than a GUI? Why worse?
- Kicking off multi-week "boot camp" to get everyone up to speed
    - Based on knowledge required to be a good intern at AWS
    - Going to keep doing Python problem sets so skills don't atrophy
- Open up command-line and do some examples
    - Where to find terminal for various systems
    - Explore directory structure of computer
        - Mirror changes in GUI so you can see the changes
        - `ls`/`cd`/`mkdir`/`pwd`/`mv`
            - **Make sure** to do a `mv` since comes up in game
        - Draw file structure on board and explain going up/down
        - **DO NOT** talk about absolute vs. relative
    - Computer is like one big tree
        - Mac is easy since based off Unix
        - Windows is harder...
            - Story of powershell and the `/` vs. the `\`
- Quick review of important commands
- Introduce `GameShell`
    - Importance of `gsh check` and `gsh goal`
    - Do first goal together
    - Come back and talk about mission 3 and mission 6 together
        - Third goal is stupid and confusing
        - Reconvene after hear complaint from ~second person
- Find lab computer to work on
    - **Work in pairs**
    - Switch every time complete "mission"
- Go!
- Reflection
    - Show GameShell on GitHub
    - Problems people had?
    - Questions people had?

### Homework

- Schoology Assessment `assessment.md`

## Resources / Random ideas

- https://www.codecademy.com/courses/learn-the-command-line/lessons/navigation
- http://web.mit.edu/mprat/Public/web/Terminus/Web/main.html
    - Seems buggy upon inspection
