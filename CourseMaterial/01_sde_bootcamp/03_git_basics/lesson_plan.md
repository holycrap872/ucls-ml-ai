## Essential Questions

- What are the benefits of version controlling your software?
- What are the basic `git` commands to setup and add to a repository?

## Lesson Plan

The goal of this lesson is to introduce students to git. I _do not_ want them to
be git experts coming out of this. Instead, I would like them to know why git is
important and to understand in general how git is a chain of diffs. With that
foundation, we can emphasize certain aspects of git in future lessons as they
are needed. In summary, as long as they understand the "graph" concept and the
`git log` concept, then I'm happy.

### Setup

- `git_cheatsheet.docx` printed out for students to use
- Various `git` learning sites loaded up
    - http://git-school.github.io/visualizing-git/ (requires Chrome)
    - https://docs.google.com/document/d/1kv9eGOh2T1Kr3K7YNIEm_U7-RmefU2ErWha9lOEuQKQ (for history)
- A few example git repositories to chew on.
    - https://gitlab.ucls.uchicago.edu/ml-ai/git-example
- Schoology Assessment on `git` published

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
        - How do we collaborate?
        - Who did what?
    - Where have you seen a solution to this?
        - GoogleDocs version history
            - Show GoogleDocs version history
                - https://docs.google.com/document/d/1kv9eGOh2T1Kr3K7YNIEm_U7-RmefU2ErWha9lOEuQKQ
            - Compare with `git`
- What do we know about `git`?
    - `git` is version control for a whole project
    - Why do you think so popular?
    - Show visual: http://git-school.github.io/visualizing-git/
        - Really can just do `git commit` for now
        - Show `git branch` but make clear don't need it until later
            - Mostly to show difference between `git` and GoogleDocs
- Essence of git
    - This is HARD... biggest lift all year
        - Real payoff in real world
    - Make small changes over time
        - Diffs!
    - Boring/hard, so take 2 min to refocus ... chat with neighbor in interim
- Do super simple example on board (drawing over `git_cheatsheet.docx` visual)
    1. Create new repo
    2. `touch new.py` and commit with message "first"
    3. `touch other.py` and commit with message "second"
    4. Edit both files and commit with message "done
- Recreate what did on board on computer
    - **Have them follow on the sheet**
        - `git_cheatsheet.docx`
    - Steps
    - Staging area -> makes for pretty commits
- Can leave early
    - DON'T DO ASSESSMENT right away b/c then information sets in brain better

### Homework

- Schoology assessment on `git`

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
