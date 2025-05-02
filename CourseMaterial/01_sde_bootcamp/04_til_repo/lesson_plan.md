## Essential Questions

- How we utilize git remote repositories?
- What practices can I adopt to make my knowledge easily viewable and sharable?

## Lesson Plan

The goal here is to show students how `git` can go from a "local" repository to
a "remote" repository. To do this, students will build on (and push) a "Today I
Learned" skeleton. This project will then be something that they to throughout
the entire class and is designed to solidify their knowledge on tricky subjects.

> Note: Student's creds (LDAP) _should_ work with `gitlab.ucls.uchicago.edu`
> Note: If have issues during setup, check `resources/common_problems/git_problems.md`

### Setup

- `Today I Learned Repo Worksheet` GoogleDoc loaded up into Schoology
    - https://docs.google.com/document/d/1sKxsWjRBgt2ABAfRx6tLGViUGiLQBp8gdnEpSM6PgBk
- `TILSkeleton` zipped and loaded onto Schoology
    - Taken from `https://gitlab.ucls.uchicago.edu/ml-ai/til`
    - `.git` folder removed
- Demo websites loaded up
    - http://git-school.github.io/visualizing-git/
    - https://github.com/jbranchaud/til
    - https://gitlab.ucls.uchicago.edu/vdangi/til
    - https://markdownlivepreview.com/

### Actual Lesson

- Review
    - `git` in comparison to GoogleDocs
    - `git` is just a bunch of diffs
    - Staged changes vs. unstaged changes
    - Show them state of ML/AI repo
        - `git diff` should show something
        - Show them what it looks like in `vscode`
- Today going to create long-running "knowledge tracker"
    - Uses git
    - Will push repository to cloud so can't be lost
    - `git push` and `git pull`
        - Caution that `git pull` is later
- Show inspiration
    - https://github.com/jbranchaud/til
        - Great long term learning technique
        - Useful whether you go into CS or not
    - Walk through various things
    - How is GitLab similar to GitHub?
- Show some examples in gitlab
    - https://gitlab.ucls.uchicago.edu/vdangi/til
    - Look at commits to see what's going on
- Markdown
    - What is it
    - How it works
    - Show some small examples
    - Raw vs. rendered
        - https://markdownlivepreview.com
- Goal today: Create your own TIL repo
    - Walk through `Today I Learned Repo Worksheet`
    - Explain things to be careful of
- Go!
    - After ~5m of them working independently, bring them back
        - Discuss confusion
        - Do first two problems as a class

### Homework

- Finish `Today I Learned Repo Worksheet`
