## Essential Questions

- What does it mean to "write a test that captures a bug"?
- How do you turn an abstract "this is wrong" into something a computer can check?

## Lesson Plan

In this lesson, students clone `ucls-hacker-functions`, pick a tier matched to
their skill level, and work through the red→green workflow locally: write a
test that captures the bug → run pytest → watch it fail → fix the function →
run pytest → watch it pass. This is the first time in the course where students
experience tests *finding* something they didn't already know was broken.

The functions are tiered (easy, medium, hard, xtreme). Students self-select.
Xtreme is **bonus only** — historical bugs that require domain context.

> Note: This lesson plan and the accompanying lesson are mostly AI generated.
  I'm not actually sure I want to do the red->green loop. Instead it's almost
  certainly better on just having the students write tests.

### Setup

- `Hacker Functions Worksheet` posted to Schoology
    - TODO: The worksheet is AI generated and **NEEDS WORK**
    - https://docs.google.com/document/d/1V-Hog5qa5YbmaGhfz3f21oAkO7rzTku-Y-E36wmYKVc
- `ucls-hacker-functions.zip` distributed via Schoology
    - Strip `.git`, `.venv`, `__pycache__`, `.coverage`, `.pytest_cache` before zipping
- `fn_01_easy.py` `can_ride_coaster` loaded on the projector for the demo
    - Forward reference: students saw this exact function in Unit 0, lesson 07
- `common_problems/venv_problems.md` ready for predictable friction
  (Windows activation syntax, network-blocked pip)

### Actual Lesson

- Project setup (~15m)
    - Students work through Setup steps 1-8 on the worksheet
    - Pair faster setups with stragglers
    - Walk around for predictable friction (see `common_problems/venv_problems.md`)
- Demo: the full red→green loop (~10m)
    - Live demo; students follow along on worksheet Problem 1
    - Open `can_ride_coaster` in `fn_01_easy.py` on the projector
    - "Some of you wrote a test for this in Unit 0. Today we make it run."
    - Write a new test (without xfail), run pytest, watch it FAIL (red)
    - Fix the function (`or` → `and`), run pytest, watch it PASS (green)
    - **The workflow:**
        - The failing test proves you found the bug
        - The passing-after-fix proves you fixed it
        - Together: the bug can never come back without someone noticing
- Tier selection (~5m)
    - See worksheet Problem 2 for tier descriptions
    - Each function's docstring describes the bug. Use it as a hint, or cover it and try to find the bug cold.
- Self-paced work (~15m)
    - Students complete worksheet Problem 2 (at least one red/green pair)
    - Walk around, prompt where stuck
    - When pytest goes green, ask: "Are you sure? What *other* inputs would catch the same bug? What does your test miss?"
- Reflection (~5m)
    - Lead class discussion on worksheet Problem 3
    - Especially the CI/CD callback (Problem 3, question 3) and automation bias
    - Anyone fix the function in a way that passed *their* test but still has a bug for inputs they didn't think of?
    - That's **automation bias** at small scale: trusting your own green when green only means "what you wrote agrees with itself."

### Homework

- TIL entry on what a "red/green test" means and why both halves matter

### Extensions / Bonus

- Try one xtreme function. Pick what interests you; don't try to do them all.
- Approachable entry points: `process_date` (Y2K), `zune_day_of_year`
- Deep-end (probably skip unless really curious): `read_memory`, `Therac25`,
  `MarsPathfinder`
