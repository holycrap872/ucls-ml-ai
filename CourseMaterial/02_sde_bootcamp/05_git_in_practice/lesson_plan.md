## Essential Questions

- How we utilize git remote repositories?
- What is the best way to save our work?

## Lesson Plan

### Setup

- Make sure that students are a part of the ML/AI group in GitLab

### Actual Lesson

- Review
    - What is your mental model of shell?
        - Navigating nice clean tree
        - I noticed all of yours are INSANE!!!
    - What is your mental model of git?
        - Git as a rock-climber
            - Search space trying to find global maxima (perfect program)
            - Commits are where you "clip in"
            - Git lets you make leaps without a worry
- Magic of `git push`
    - You're on the "main" branch... don't really want to get into branches
    - Push the branch you're on
    - Push and look at people's TIL
- Last class, created a remote repository for TIL
    - Now going to create remote repository for ProblemSet
    - Create "New project" -> "Create blank project" in Gitlab
        - Make sure private
        - Make sure README is NOT checked
        - Give me access
- Class work
    - Create an ml-ai folder in Documents/workspace/2023-24/lab_school
        - Make me a `Maintainer`
    - Move all previous projects into this folder
        - TIL and Problem Skeleton
    - Create an "initial commit" for your Problem Set Skeleton
        - `git init` and `git add`
        - I very sneakily put a .gitignore file in the problem set skeleton
    - Push "initial commit" to your GitLab Problem Set repo
    - Start homework

### Homework

- Do problems X-X of Python String Wheaties
- For each problem, create a commit
- Every time create a commit, push it to main so you don't lose your work
