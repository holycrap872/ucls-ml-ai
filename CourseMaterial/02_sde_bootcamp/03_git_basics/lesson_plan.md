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
    - What is command-line?
    - Why do we need command-line?
    - Do a quick example as a class
        - `touch` a file
        - `mkdir` a directory
        - `mv` file into directory
- What is "version control"?
    - Show graphic of a file with a bunch of prefixes like "_v4_Final"
    - What's the problem?
        - Which version is the latest?
        - What changed?
        - How do we Collaborate?
        - Who did what?
    - Where have you seen a solution to this?
        - GoogleDocs version history
            - Show GoogleDocs version history
            - Compare with Git
- What do we know about `git`?
    - Git is version control for a whole project
    - Why do you think so popular?
    - Show visual: http://git-school.github.io/visualizing-git/
        - Really can just do `git commit` for now
- What do you notice about a real git repository?
    - https://gitlab.ucls.uchicago.edu/ml-ai/git-example
    - Have click around for 3-5 minutes
        - notice/wonder
- Essence of git
    - This is HARD... biggest lift all year
        - Real payoff in real world
    - Make small changes over time
        - Diffs!
    - Show example diffs from shell exercise
    - Draw as a network/graph
    - Show equivalent in git: https://gitlab.ucls.uchicago.edu/ml-ai/git-example
        - How is this similar to GoogleDocs?
- Do super simple example
    - Word ladder
    - **Have them follow on the sheet**
        - `git_cheatsheet.docx`
    - Staging area -> makes for pretty commits
- What do you think we're going to use git for?
    - Problem sets
    - TIL
        - Show Josh's TIL: https://github.com/jbranchaud/til
        - 11k stars

### Homework

- Schoology assessment on `git`
    - Watch video first

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
- https://ohmygit.org/press/
    - Game about git
