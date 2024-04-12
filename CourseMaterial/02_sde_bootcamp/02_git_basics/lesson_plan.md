## Essential Questions

- What are the benefits of version controlling your software?
- Why are diffs such a powerful primitive?

## Lesson Plan

The goal of this lesson is to introduce students to git. I _do not_ want them to
be git experts coming out of this. Instead, I would like them to know why git is
important and to understand in general how git is a chain of diffs. With that
foundation, we can emphasize certain aspects of git in future lessons as they
are needed. In summary, as long as they understand the "graph" concept and the
`git log` concept, then I'm happy.

### Setup

A few example git repositories to chew on.

### Actual Lesson

- Reflection from previous lesson
    - What is shell?
    - Why do we need shell?
    - Watch video as a class
        - https://www.youtube.com/watch?v=ephId3mYu9o
        - Discuss
    - Do a quick example as a class.
- What do we know about git?
    - Version control
    - Totally dominated/took over
        - Interesting history w/ Linus Torvald
    - Why do you think so popular?
    - Git check -> who has `git` on command line?
        - They all _should_ have `git` on the command line because of vscode
- What do you notice about a real git repository?
    - https://gitlab.ucls.uchicago.edu/ml-ai/git-example
    - Have click around for 3-5 minutes
- Why git?
    - Make small changes over time
    - Track who's making changes
    - Easily go back in history
    - How similar/how different to GoogleDocs history
- Essence of git
    - Diffs!
    - Show example diffs from shell exercise
    - Draw as a network/graph
    - Show equivalent in git: https://gitlab.ucls.uchicago.edu/ml-ai/git-example
        - How is this similar to GoogleDocs?
- Do super simple example
    - Word ladder
    - **Have them follow on the sheet**
    - Staging area -> makes for pretty commits
- What do you think we're going to use git for?
    - Problem sets
    - TIL
        - Show Josh's TIL: https://github.com/jbranchaud/til
        - 11k stars

### Homework

- Turn Problem Set Skeleton into git repo
    1. `git init`
    2. Add any and all useful files (nothing with a `.` in front of it)
        - I very sneakily put a .gitignore file in the problem set skeleton
    3. Create "initial commit"
    4. Do a **single** problem from Wheaties
    5. Create second commit

### Resources

- https://youtu.be/8JJ101D3knE
    - Good general introduction up to minute 6
    - Make clear get bonus points (fake) if can do it on command-line
- https://youtu.be/i_23KUAEtUM
    - Git for vscode
    - Kind of relies on you knowing git/purpose of git
    - Not sure how much git knowledge people have
- https://www.youtube.com/watch?v=USjZcfj8yxE
    - 15m intro to git
