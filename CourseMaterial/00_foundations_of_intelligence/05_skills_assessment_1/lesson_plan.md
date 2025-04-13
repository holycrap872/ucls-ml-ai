## Essential Questions

- What do we want to remember?
- What do we actually remember?

## Lesson Plan

This is the first attempt at being technical in the class. The goal is to
figure out where the students are along several dimensions:

1. How well do they setup a project's environment?
2. How much do they remember about programming?
3. What other things do I not know about?

For coding, students will be using the `ProblemSetSkeleton`. The skeleton has
GitLab CI/CD logic included in it (but don't tell the students that yet). The
overall goal this class is to get their local development environment set up.
In future classes, they will:

1. Learn about `git` and will therefore turn `ProblemSetSkeleton` into a git repo
2. Learn about remote repositories and there push `ProblemSetSkeleton` to GitLab
3. Learn about CI/CD and therefore come to understand what's in the `.ci-cd` folder

For now, though, just tell them to focus on the `src` and `tests` directories
and that everything else in `ProblemSetSkeleton` will be explained later.

### Setup

- `./chatbot_output_python/landscape_game.py` printed out
- `ProblemSetSkeleton` zipped and loaded into Schoology
    - https://gitlab.com/eric.rizzi/problem-set-skeleton
    - Cleanup and remove unnecessary files:
        - `rm -rf .git && rm -rf .venv && rm -rf .pytest_cache && rm coverage.xml && rm .coverage`
        - `find . -name "__pycache__" -exec rm -r {} \;`
        - `find . -name ".DS_Store" -exec rm -r {} \;`
    - Verify future necessary files are still present before zipping:
        - `.ci-cd`
        - `.vscode`
        - `data`
            - `data/text/great_gatsby.txt`
            - `data/text/little_women.txt`
- `Skills Assessment Worksheet` posted on Schoology
    - https://docs.google.com/document/d/1qt4WpGlUJX_-c_pszl-Al2Y12nbc3wcpDWMTOKnE-hw

### Actual Lesson

- Reflection
    - Discussion
        - Hand back graded discussion rubrics
    - Who was Turing?
    - What was his test?
    - What did we learn?
    - What is machine learning?
        - Program, data, and feedback
- Setup skills assessment
    - Today going to see how far you can get programming stuff
    - No pressure at all
- What do we remember about Python?
    - primitives
    - variables
    - lists
- Walk through `landscape_game.py` to further jog memory
    - JavaScript and Python are similar
    - What do you recognize/see from Python
    - What is happening on lines x, y, z?
- IDE
    - Brief history of IDE
    - Modern day IDE's are like a bento box
    - All parts of development in one place
        - Used to have to use multiple different programs
- Walk through VSCode setup
    - Who was able to install everything?
    - Install necessary extensions and get running
        - Python Extension
        - Black Formatter
        - Isort
        - Pylance
    - Do simple programs as a class
        - Get everyone running a simple "hello world" program
        - Take in numbers from user until they hit "q" and then sums then
    - Highlight what extensions are doing
- Download and setup `ProblemSetSkeleton`
    - Importance of being in workspace
        - **Make sure to click on** `ps-skeleton.code-workspace`
        - Get bunch of advanced features
        - Note to instructor: Check that people have proper setup repeatedly over coming days
    - Ignore files you don't understand
        - e.g., `.ci-cd`
- Get started on `Skills Assessment Worksheet`
    - Walk through worksheet
    - Break up into pairs based on skill level
    - Walk around prodding people to improve practices in various ways

### Homework

- Finish problems 0 and 1 of Skills Assessment (aka the first two problems)
