## Essential Questions

- How can we use the command-line to increase our effectiveness?
- How much effort should I put into understanding the tools I'm using?

## Lesson Plan

### Setup

- Terminals open on desktop computers in lab
    - Command `ssh -p 2220 bandit0@bandit.labs.overthewire.org` typed in
- `Git Kickoff Worksheet` loaded into Schoology
    - https://docs.google.com/document/d/1JKkWEULvgkRLH8VBuKTFchZi8yxuXm6Nm9RLyv2UeFI

### Actual Lesson

- Review
    - Commands
        - `ls`, `cat`, `cd`, `touch`, etc.
    - Paths
        - `mkdir hey && touch hey/file.txt vs. mkdir hey && cd hey && touch file.txt`
        - Hacking websites via path traversal
            - https://finance.yahoo.com/screener/..
- Review homework
    - Do problem 4 as a class
        - Go around room asking "what next"
    - Have terminal in front of GoogleDoc so easy to see what needs to be done next
- Why terminal?
    - Stress that important if ever going to do CS
        - One of 2-3 fundamental tools
    - Show xkcd comic: https://xkcd.com/519/
- Can understand VSCode better now that know terminal
    - Create file via GUI
        - Equivalent to: `ProblemSetSkeleton` -> `touch`
    - Run program via GUI
        - Equivalent to: `python3 ....`
    - Overall point: many VSCode commands actually running terminal commands
- `ssh`
    - Foundation of internet
    - Allows you to connect to another person's computer
    - Draw two computers connecting
- `overthewire.org`
    - Today going to do one final shell activity
    - Show `ssh -p 2220 bandit0@bandit.labs.overthewire.org`
        - Explain what each part means
    - Going to accomplish various tasks
    - demo
- Show website
    - Solve first two together as class
        - the `./-` in level 1 is ANNOYING
- Break up in to pairs
    - Go!
- Setup homework
    - Going to be about a tool called `git`
    - It's a way to save changes in project
    - Very similar to version history in GoogleDocs
    - Will build on initial understanding from worksheet in class tomorrow

### Homework

- `Git Kickoff Worksheet`
    - Note: I haven't actually done this in a real class yet
        - The goal is to expose them to `git` and have them thinking about it
        - Honestly not sure if this is the best way to prep them
