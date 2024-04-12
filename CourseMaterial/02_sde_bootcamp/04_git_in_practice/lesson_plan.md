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
- Last class, pulled down a repo gitlab created
    - Now going to push up a repo we created in our local
        - What's the difference between these two things?
    - Create "New project" -> "Create blank project" in Gitlab
        - Make sure private
        - Make sure README is NOT checked
        - Give me access
- Class work
    - Create an ml-ai folder in Documents/workspace/2023-24/lab_school
    - Move all previous projects into this folder
        - TIL and Problem Skeleton
        - Make me a `Maintainer`
    - Make a "pipeline status badge"
        - Badge Name: Build Status
        - Badge Link: https://gitlab.ucls.uchicago.edu/%{project_path}/-/commits/%{default_branch}
        - Badge image URL: https://gitlab.ucls.uchicago.edu/%{project_path}/badges/%{default_branch}/pipeline.svg
        - Note: I'm not sure why they make it so annoying
    - Make a "coverage badge"
        - Badge Name: Code Coverage
        - Badge Link: https://gitlab.ucls.uchicago.edu/%{project_path}/-/commits/%{default_branch}
        - Badge image URL: https://gitlab.ucls.uchicago.edu/%{project_path}/badges/%{default_branch}/coverage.svg
    - Create an "initial commit" for your Problem Set Skeleton
        - `git init` and `git add`
        - Do not commit any hidden files/folders (leading “.”) 
    - Push "initial commit" to your GitLab Problem Set repo
    - Create a README.md for your Problem set and commit it
        - Browser https://conventionalcomments.org/ to understand the type of feedback I'll leave
    - Start homework

### Homework

- Do problems 7-11 of Python String Wheaties
- For each problem, create a commit
- Every time create a commit, push it to main so you don't lose your work
