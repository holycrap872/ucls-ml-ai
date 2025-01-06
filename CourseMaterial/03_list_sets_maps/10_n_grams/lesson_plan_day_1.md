## Essential Questions

- How do we create a Markov model?
- How can we use a Markov model to drive text generation?

## Lesson Plan

In this lesson, students reflect on the strengths/weaknesses of the ChatBots
they build in the previous unit. Then, we discuss ways to improve the bots to
make them much more realistic. Finally, the students start to debug a broken
version of an n-gram markov model program.

This lesson serves three purposes:
1. It makes up for the fact that a lot of students would struggle to create a
   fully probabilistic n-gram Markov model without a ton of time.
2. Students are coming back from break around this point and have forgotten
   a lot.
3. Prior to the break, there are usually a lot of absences/illnesses, so
   providing some example code for the students who missed to "build off of" as
   they complete the worksheet from the previous unit is helpful

### Setup

- `broken_mm_structured.zip` and `broken_mm_unstructured.zip` posted to Schoology
    - TODO: Broken MM project ready for cloning
- Markov Model site loaded up
    - https://www.cs.cmu.edu/~dst/MarkovChainDemo/

### Actual Lesson

- Review
    - FSMs
    - Markov models
        - Purpose
        - Creation
        - Traversal
    - Go through someone's example
        - If no one is done, look at `../09_markov_chain/markov_predict_text.py`
- Reflection
    - How is this ChatBot similar to real ChatBots?
    - What was hard about programming it?
    - What are deficiencies from our example and real Markov Model?
        - Wasn't recording probability
        - Not much "context"
        - How might overcome these problems?
- N-grams
    - How they work
    - Work through simple example:
        - "i like dogs i like cats i don't like fish"
        - 1-gram
        - 2-gram
        - Graphs start to hold context
    - Show https://www.cs.cmu.edu/~dst/MarkovChainDemo/
        - Do for various grams
- Setup for the day
    - Have another "broken" bit of software
    - Your could is to get it working
- Quick debugging refresher using breakpoints
- Go!
    - Split up **into pairs**
    - Switch who's on the keyboard every 5 minutes

### Homework

- Data Structure Wheaties 22

### Extensions

- Formally define the behavior in terms of probability
    - Bayes
- https://towardsdatascience.com/text-generation-using-n-gram-model-8d12d9802aa0
- https://www.cs.cmu.edu/~dst/MarkovChainDemo/

### Missed class

- https://www.youtube.com/watch?v=MGVdu39gT6k
    - 6:37 - end
