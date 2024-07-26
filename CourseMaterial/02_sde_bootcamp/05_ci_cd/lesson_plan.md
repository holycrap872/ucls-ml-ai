## Essential Questions

- How can I design programs to minimize the chance of errors?

## Lesson Plan

In this class, students set up their ProblemSetSkeleton repository to be able
to doing CI/CD. In the process, students will come to understand why this is so
important in terms of engineering excellence. Finally, they will practice using
the CI/CD integration by writing tests and checking the results after they push.

### Setup

- `.ci-cd` folder zipped in Schoology

### Actual Lesson

- Review
    - git
    - remote vs. local
    - commits
    - Examine someone's 
    - Beauty of python
        - https://peps.python.org/pep-0020/
- CI/CD
    - Discuss
    - Show examples in github/gitlab
    - Programming vs. Engineering
- Set up ProblemSetSkeleton
    - Copy in `.ci-cd` folder
    - Make a "pipeline status badge"
        - Badge Name: Build Status
        - Badge Link: https://gitlab.ucls.uchicago.edu/%{project_path}/-/commits/%{default_branch}
        - Badge image URL: https://gitlab.ucls.uchicago.edu/%{project_path}/badges/%{default_branch}/pipeline.svg
        - Note: I'm not sure why they make it so annoying
    - Make a "coverage badge"
        - Badge Name: Code Coverage
        - Badge Link: https://gitlab.ucls.uchicago.edu/%{project_path}/-/commits/%{default_branch}
        - Badge image URL: https://gitlab.ucls.uchicago.edu/%{project_path}/badges/%{default_branch}/coverage.svg
- Class work

### Homework

- Do problems X-X of ???
- For each problem, create a commit
- Every time create a commit, push it to main so you don't lose your work
    - Every time you push, check that CI/CD stuff is there

### Resources

- https://www.conventionalcommits.org/en/v1.0.0/
- Turn on CI/CD
