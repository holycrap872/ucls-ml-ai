## Essential Questions

- When are lists, sets, or maps most effective?
- How can we use data to make predictions?

## Lesson Plan

### Setup

- Solution associated with "Nerd Dice" lesson printed out so students can analyze it
    - `nerd_dice_solution.py`
- `Text Analysis Worksheet` posted to Schoology
    - Structured: https://docs.google.com/document/d/16RyyfLeFgYusdKyLlAZVpPn_eaLOoWZdl4A4x_U852I
    - Unstructured: https://docs.google.com/document/d/1-v7pL5HZumD5vZaz0Xomjl-1uwfqtEiB3n031yuksLY

### Actual Lesson

- Reflection
    - When to use sets/maps/lists?
    - What is a count dict?
- Code discussion
    - Hand out _my_ solution for "Nerd Dice" worksheet: `nerd_dice_solution.py`
    - Discuss
        - 2 things you're happy you did the same as me
        - 2 things you wish you had done
- Sets
    - Sets a groups of things that share given property
        - infinite or finite
    - Draw venn diagram
    - Do example:
        - Set of words with "a" 
        - Set of words that start with "b"
- Set operations
    - intersection
    - union
    - diff
    - Do some examples in the python REPL
- Introduce problem
    - Previous problem (plotting classics)
    - Over next few days, going to compare books over the decades to understand how language changes
    - https://xkcd.com/1007/
    - Going to use that to build a "decade prediction" engine
- Discuss intent of problem
    - Show discussion with ChatGPT about good stuff for project
    - Have them read through worksheet and ask questions
- Have them pick their own set of books from two different decades
    - Stress 1920's or prior (copyright issues)
    - Compare which books/decades and why
- Start worksheet
    - Four things to do about before starting any project
        1. New file
        2. Look for where done it before
        3. Identify/research libraries to use
        3. Identify/research useful functions
            - `load_text_from_book()`
            - `text_to_words()`
            - `get_count_dict()`
    - Go!

### Homework

- TIL on set operations
- Data Structure Wheaties 14 - 15
