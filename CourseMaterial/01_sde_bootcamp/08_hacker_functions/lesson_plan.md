## Essential Questions

- Why are tests so important?
- How do you turn an abstract "this is wrong" into something a computer can check?
- What does encoding past failures say about problem-solving?

## Lesson Plan

In this lesson, students clone `ucls-hacker-functions`, pick a tier matched to
their skill level, and work through each problem. This is the first time in the
course where students experience tests *finding* something they didn't already
know was broken. The goal is have the students appreciate that tests are a form
of "specification" and capturing bugs in tests prevents similar issues from
happening again.

### Setup

- `Hacker Functions Worksheet` posted to Schoology
    - TODO: The worksheet is AI generated and **NEEDS WORK**
    - https://docs.google.com/document/d/1V-Hog5qa5YbmaGhfz3f21oAkO7rzTku-Y-E36wmYKVc
- `ucls-hacker-functions.zip` distributed via Schoology
    - Strip `.git`, `.venv`, `__pycache__`, `.coverage`, `.pytest_cache` before zipping
- `fn_01_easy.py:can_ride_coaster` loaded on the projector for demo
    - Forward reference: students saw this exact function in Unit 0, lesson 07
- `resources/common_problems/venv_problems.md` ready for fast debugging

### Actual Lesson

- Review
    - CI/CD
    - Spin the wheel for someone's string problems
        - Look at status of individual commits
        - Look at actual problems
        - Look at tests
- Discussion testing
    - How viewed it so far?
    - How real engineers view it
        - In some ways more important than code
        - Actionable memory of everything you got wrong in the past
        - Concept of a Red -> Green test converging on correctness
        - Tests as bait for disagreement: write the test that captures *your* understanding, see what fails
        - That works against your own code; it also works against AI's (preview of next class)
- Hacker functions
    - Open `can_ride_coaster` in `fn_01_easy.py` on the projector
    - "Some of you wrote a test for this in Unit 0. Today we make it run."
    - Write a new test (without xfail), run pytest, watch it FAIL (red)
    - Fix the function (`or` → `and`), run pytest, watch it PASS (green)
    - **The workflow:**
        - The failing test proves you found the bug
        - The passing-after-fix proves you fixed it
        - Together: the bug can never come back without someone noticing
    - Each function's docstring describes the bug. Use it as a hint, or cover it and try to find the bug cold.
- Tier selection
    - Describe tiers and break up into pairs based on matching difficulty levels
    - Brag about the extreme a bit since it's about historical bugs
    - Break up into pairs 
- Start classwork
    - Work through GoogleDoc to get started
    - Walk around for predictable friction (see `common_problems/venv_problems.md`)
- Reflection
    - Lead class discussion on worksheet Problem 3
    - Especially the CI/CD callback (Problem 3, question 3) and automation bias
    - Anyone fix the function in a way that passed *their* test but still has a bug for inputs they didn't think of?

### Homework

- TIL entry on what a "red/green test" means and why both halves matter

### Extensions / Bonus

- Try one xtreme function. Pick what interests you; don't try to do them all.
- Approachable entry points: `process_date` (Y2K), `zune_day_of_year`
- Deep-end (probably skip unless really curious): `read_memory`, `Therac25`,
  `MarsPathfinder`
