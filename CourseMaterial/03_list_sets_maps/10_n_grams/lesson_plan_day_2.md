## Essential Questions

- How do we mathematically represent a Markov chain?
- How can we add some amount of context to Markov chains?

## Lesson Plan

### Setup

- None

### Actual Lesson

- Review
    - Graphs
    - Markov chains
    - Tokens
    - n-grams
- Markov chain implementation
    - Where did we leave off?
    - Difficult / easy parts
    - Show volunteer's code as of now
- Finish debugging activity
    - Work in pairs
- Discussion
    - Think/write for 5-10 minutes then discuss
    - EQ's:
        - How does this compare with your experience of how ChatBots programmed?
        - How does this compare with your experience of how ChatBots trained?
        - How does this compare to your experience using ChatBots?
    - Show quote from Turing's Computer Intelligence article
        - Which part of what we did is the "Child Programme"
        - Which part is the "education process"?

### Homework

- Data structures problem set

### Extensions

- Markov chain formalization
    - Conditional Probability
    - Markov Property:
        - "knowledge of the previous state is all that's necessary to find probability distribution of the current state"
        - https://brilliant.org/wiki/markov-chains/
- Add a special "stop" character to identify the end of a sentence.
- Use topic modeling to identify the main topics in a conversation and steer the
  chatbot's responses in a direction more aligned with the current topic of discussion.
- Develop a back-off model where if an n-gram isn't found, the model backs off
  to a (n-1)-gram model for predictions, and so on.
- "LaPlace smoothing"