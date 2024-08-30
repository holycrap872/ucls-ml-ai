## Essential Questions

- How can we use terminal to increase our effectiveness?
- How much effort should I put into understanding the tools I'm using?

## Day 1 Lesson Plan

On the first day, we will discuss how powerful (and confusing) the command-line
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

## Day 2 Lesson Plan

In this class, students formalize the knowledge they gained while playing
`GameShell` the previous day. After the review/discussion students will start
a command-line worksheet that will make the concepts more grounded.

### Setup

- Harry Potter Docker image ready to run
    - https://hub.docker.com/repository/docker/erizzi/hp_terminal_tutorial
- Command-Line Worksheet posted to Schoology
    - https://docs.google.com/document/d/1vkbXWdJovLMV1-w6NBhE25EzL_QALkfkZXIRrygZy_Y
- `cmd_line_exercise.zip` posted to Schoology

### Actual Lesson

- Review
    - Why shell is useful
    - GameShell commands
    - GameShell file structure
    - Real computer's file structure
    - Harry Potter in MS
        - Various commands/mnemonics
- Mastering shell
    - 100's of commands
    - Command-line editors
        - `vim` and `nano` and `emacs`
    - Story of ctrl-r
        - Trade off between doing what you know and learning new things
- Draw a tree structure and explain relative/absolute of `GameShell`
    - Show all the libraries
    - Show that folder structure is the same in websites and in terminal
        - https://github.com/phyver/GameShell
- Hand out command-line worksheet
    - Read through the introduction together
- Go!

### Homework

- Finish worksheet

## Resources / Random ideas

- https://www.codecademy.com/courses/learn-the-command-line/lessons/navigation
- http://web.mit.edu/mprat/Public/web/Terminus/Web/main.html
