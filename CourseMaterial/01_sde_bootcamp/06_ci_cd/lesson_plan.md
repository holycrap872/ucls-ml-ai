## Essential Questions

- How can I design programs to minimize the chance of errors?

## Lesson Plan

In this class, students set up their `ProblemSetSkeleton` repository to be able
to CI/CD. In the process, students will come to understand why this is so
important in terms of "engineering excellence". Finally, they will practice using
the CI/CD integration by writing tests and checking the results after they push.

### Setup

- None

### Actual Lesson

- Review
    - git
    - remote vs. local
    - commits
- TIL review
    - Importance of TIL
    - Show rubric
    - Examine someone's entry
        - Compare against rubric
- Code review
    - First set up perms
        - Why "private"?
        - Walk them through giving me access to their repo
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
- Setup classwork
    - Why wheaties?
    - Possibility of doing Grok if would like refresher
- Reflection
    - Where are we?
    - What's next?
        - Start data analysis unit
- Start classwork

### Homework

- Do problems X-X of ???
- For each problem, create a commit
- Every time create a commit, push it to main so you don't lose your work
    - Every time you push, check that CI/CD stuff is there

### Resources

- https://www.conventionalcommits.org/en/v1.0.0/
- Turn on CI/CD

### Extensions

- Pipeline Badges
    - Make a "pipeline status badge"
        - Badge Name: Build Status
        - Badge Link: https://gitlab.ucls.uchicago.edu/%{project_path}/-/commits/%{default_branch}
        - Badge image URL: https://gitlab.ucls.uchicago.edu/%{project_path}/badges/%{default_branch}/pipeline.svg
        - Note: I'm not sure why they make it so annoying
    - Make a "coverage badge"
        - Badge Name: Code Coverage
        - Badge Link: https://gitlab.ucls.uchicago.edu/%{project_path}/-/commits/%{default_branch}
        - Badge image URL: https://gitlab.ucls.uchicago.edu/%{project_path}/badges/%{default_branch}/coverage.svg