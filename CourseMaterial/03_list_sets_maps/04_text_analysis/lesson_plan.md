## Essential Questions

- When are lists, sets, or maps most effective?
- How can we use data to make predictions?

## Lesson Plan

### Setup

Print out text analysis sheet

### Actual Lesson

- Reflection
    - When to use sets/maps/lists?
    - What is a count dict?
- Sets
    - intersection
    - union
    - diff
    - Draw venn diagram
        - Have them do it in their notes as well
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

### Possible extensions
- Book to book comparison
    - GrammaTech Index generator
    - What are the types of words that are most common in one book but aren't in another?
    - Character comparisons (z's vs a's)
- Decade to decade comparison:
    - Words used more than 5 times in each book from one decade not used at all in another
    - Most used word from one decade that wasn't used at all in previous decade
- Multiple decade comparison
    - Graph use of a particular word over time (like xkcd)
    - Length of sentences across decades
