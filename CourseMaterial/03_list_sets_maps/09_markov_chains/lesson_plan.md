## Essential Questions

## Lesson Plan

### Setup

`ana_markov_sim.py` seeded with intentional error where `ana_location = next_stop` is missing

### Actual Lesson

- Review
    - TIL of debugging
- Today theory or chatbots, M-W chat bots
- Markov Chains
    - Discuss theory
        - https://www.youtube.com/watch?v=JHwyHIz6a8A
        - Have simple problem representing progression
            - `ana_markov.py`
            - Note: If want, seed bug by deleting `ana_location = next_stop` on line 32
    - "I like turtles" Markov chain
        - Have them come up with sample sentences using dice
        - Have them read sentences they come up with
        - First person that get's "I like turtles": https://youtu.be/CMNry4PE93Y?feature=shared&t=8
    - Markov Music
        - https://spranesh.github.io/mcmg/
        - https://youtu.be/OLNA40LpHWE?si=_p25RbPek4gKELWh&t=27
    - Markov of name
    - Markov of letters in a simple sentence
        - What to do about spaces
        - Create a graph representing simple sentence
        - Use dice to roll 
- Class work
    - Create function that creates graph representing markov of input sentence
    - Design together
    - Easy
        - Dictionary to set
    - Hard
        - Dictionary to counting dictionary
    - Test function with unit tests

##### Homework

- Finish class work

##### Missed class resource

- https://www.youtube.com/watch?v=MGVdu39gT6k
    - 0:00 - 6:37
