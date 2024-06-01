## Essential Questions

- How do we mathematically represent a Markov chain?
- How can we add some amount of context to Markov chains?

## Lesson Plan

### Setup

None

### Actual Lesson

- Review
    - Graphs
    - Markov chains
    - Tokens
    - Transistions
- Markov chain implementation
    - Where did we leave off
    - Difficult / easy parts
    - Show volunteer's code as of now
- Markov strengths/weakenesses
    - Strenths
        - Somewhat mimic the voice of a book
        - Fast/cheap compared to ChatGPT
        - Intuitive
    - Weaknesses
        - Text is confusing
        - How could we improve it?
- N-grams
    - Previously did 1-grams
    - What do you think a 2-gram would look like?
    - Two-grams add a small amount of context
    - 2-gram demo of a sentence
        - "Bright stars light dark skies, dark skies hide"
        - How would resulting 2-gram differ from 1-gram?
    - Show them my two-gram code and the actual code
        - Run it
        - Highlight that sometimes can start to repeat part of book verbatim
            - Why?
- Discussion
    - Think/write for 5-10 minutes then discuss
    - EQ's:
        - How does this compare with your experience of how ChatBots programmed?
        - How does this compare with your experience of how ChatBots trained?
        - How does this compare to your experience using ChatBots?
    - Show quote from Turing's Computer Intelligence article
        - Which part of what we did is the "Child Programme"
        - Which part is the "education process"?

#### Homework

- Finish worksheet on 1-grams and commit if didn't
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