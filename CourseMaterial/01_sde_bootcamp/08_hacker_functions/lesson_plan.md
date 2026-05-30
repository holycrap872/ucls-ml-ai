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

> Note: Setup happens in-class with teacher support. The first ~15 minutes are
  reserved for everyone to get the repo running. Pair students up so the
  faster setups can help the stragglers.

### Setup

- `ucls-hacker-functions.zip` distributed via Schoology
    - Strip `.git`, `.venv`, `__pycache__`, `.coverage`, `.pytest_cache` before zipping
- `fn_01_easy.py` `can_ride_coaster` loaded on the projector for the demo
    - Forward reference: students saw this exact function in Unit 0, lesson 07
- `common_problems/venv_problems.md` ready for predictable friction
  (Windows activation syntax, network-blocked pip)

### Actual Lesson

- Project setup (~15m)
    - Download zip from Schoology, unzip, open in VSCode
    - Create venv: `python3 -m venv .venv` → activate
    - `pip install -e ".[dev]"`
    - Verify pytest runs:
        - You'll see a mix of `PASSED` and `XFAIL`
        - `XFAIL` means "this test is expected to fail because the bug is
          still there" — those are reference tests showing the *shape* of a
          bug-catching test
    - If anything breaks, raise your hand. Pair-debug with your neighbor.
- Demo: the full red→green loop (~10m)
    - Open `can_ride_coaster` in `fn_01_easy.py`
    - "Some of you wrote a test for this in Unit 0. Today we make it run."
    - Open `tests/test_fn_01_easy.py` — find the existing `@pytest.mark.xfail`
      test for `can_ride_coaster`. That's the model.
    - Write a *new* test (without xfail) that captures the bug — pick a
      specific input that should return `False` but currently returns `True`
    - Run pytest → new test FAILS (red)
    - Fix the function (`or` → `and`)
    - Run pytest → new test PASSES (green)
    - **That's the workflow:**
        - The failing test proves you found the bug
        - The passing-after-fix proves you fixed it
        - Together: the bug can never come back without someone noticing
- Tier selection (~5m)
    - `fn_01_easy`: small bugs, 2-minute finds
    - `fn_02_medium`: same shape, harder bugs
    - `fn_03_hard`: requires dicts and loops we haven't fully covered
    - `fn_04_xtreme`: **bonus** — historical bugs (Y2K, Heartbleed, Therac-25).
      No one is expected to do these. Pick if curious.
    - Each function's docstring describes the bug. Use it as a hint, or cover
      it and try to find the bug cold.
- Self-paced work (~15m)
    - Goal: complete 1-2 red/green pairs in your chosen tier
    - Walk around, prompt where stuck
    - When pytest goes green, ask: "Are you sure? What *other* inputs would
      catch the same bug? What does your test miss?"
- Reflection (~5m)
    - Remember the line from CI/CD day — "a green pipeline isn't proof your
      code works, it's proof your tests didn't catch anything."
    - Anyone fix the function in a way that passed *their* test but still has
      a bug for inputs they didn't think of?
    - That's **automation bias** at small scale: trusting your own green when
      green only means "what you wrote agrees with itself."

### Homework

- TIL entry on what a "red/green test" means and why both halves matter

### Extensions / Bonus

- Try one xtreme function. Pick what interests you; don't try to do them all.
- Approachable entry points: `process_date` (Y2K), `zune_day_of_year`
- Deep-end (probably skip unless really curious): `read_memory`, `Therac25`,
  `MarsPathfinder`
