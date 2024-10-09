## Essential Questions

- How can I design programs to minimize the chance of errors?

## Lesson Plan

In this class, students set up their `ProblemSetSkeleton` repository to be able
to CI/CD. In the process, students will come to understand why this is so
important in terms of "engineering excellence". Finally, they will practice using
the CI/CD integration by writing tests and checking the results after they push.

### Setup

- Various CI/CD sites open
    - https://github.com/angr/angr
    - https://gitlab.com/eric.rizzi/aws-src-sample

### Actual Lesson

- Review
    - git
    - remote vs. local
    - commits
- Code review
    - Spin the wheel
    - Examine someone's code
- CI/CD
    - What is CI/CD?
    - Why CI/CD?
        - Fixes "works on my machine"
        - Single point of "correctness"
        - Break the build --> doughnuts for everyone
    - Show examples in github/gitlab
    - Programming vs. Engineering
- Set up `ProblemSetSkeleton`
    - Discuss contents of `.ci-cd` folder
        - What are the commands checking?
    - `Settings` -> `CI/CD` -> `General pipelines`
        - Add `.ci-cd/gitlab-ci.yml`
- Make sure everyone is up and running
- Reflection
    - Where are we?
    - What's next?
        - Start data analysis unit
- Start classwork

### Homework

- Do problems 5 - 8 of Python String Wheaties
    - For each problem, create a commit
    - Every time create a commit, push it to main so you don't lose your work
    - Every time you push, check that CI/CD stuff is there
- TIL on CI/CD

### Resources

- https://www.conventionalcommits.org/en/v1.0.0/
- Turn on CI/CD

### Extensions

- Pipeline Badges
    - Note: I'm not sure why they make the whole process so annoying
    - Make a "pipeline status badge"
        - Go to `Settings` -> `General` -> `Badges`
        - Badge Name: Build Status
        - Badge Link: https://gitlab.ucls.uchicago.edu/%{project_path}/-/commits/%{default_branch}
        - Badge image URL: https://gitlab.ucls.uchicago.edu/%{project_path}/badges/%{default_branch}/pipeline.svg
        - Insert into README:
            - `![pipeline status](https://gitlab.ucls.uchicago.edu/ml-ai/problem-set-skeleton/badges/main/pipeline.svg)`
    - Make a "coverage badge"
        - Go to `Settings` -> `General` -> `Badges`
        - Badge Name: Code Coverage
        - Badge Link: https://gitlab.ucls.uchicago.edu/%{project_path}/-/commits/%{default_branch}
        - Badge image URL: https://gitlab.ucls.uchicago.edu/%{project_path}/badges/%{default_branch}/coverage.svg
        - Insert into README:
            - `![coverage](https://gitlab.ucls.uchicago.edu/ml-ai/problem-set-skeleton/badges/main/coverage.svg)`