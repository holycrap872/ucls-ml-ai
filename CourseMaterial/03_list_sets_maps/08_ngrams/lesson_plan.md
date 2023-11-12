## Essential Questions

- How do we mathematically represent a Markov chain?
- How can we add some amount of context to Markov chains?

## Lesson Plan

### Setup

None

### Actual Lesson

- Review
    - Markov chains
    - Tokens
    - Transistions
    - Show my graph of the sentence
- Markov chain formalization
    - Conditional Probability
    - Markov Property:
        - "knowledge of the previous state is all that's necessary to find probability distribution of the current state"
        - https://brilliant.org/wiki/markov-chains/
- Weaknesses seen?
    - Text is confusing
    - How could we improve it?
- N-grams
    - Previously did 1-grams
    - What do you think a 2-gram would look like?
    - Two-grams add a small amount of context
    - 2-gram demo of a sentence
        - "Bright stars light dark skies, dark skies hide"
        - Have them do it on the board (use `bs`, `sl`, `ld`, ... for short)
        - How is this different from 1-gram?
- Copy code and put into new file
    - Implement

### Extensions

- Add a special "stop" character to identify the end of a sentence.
- Use topic modeling to identify the main topics in a conversation and steer the
  chatbot's responses in a direction more aligned with the current topic of discussion.
- Develop a back-off model where if an n-gram isn't found, the model backs off
  to a (n-1)-gram model for predictions, and so on.
- "LaPlace smoothing"