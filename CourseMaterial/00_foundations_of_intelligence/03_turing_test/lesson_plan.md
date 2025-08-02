## Essential Questions

- Where does consciousness lie?
- What signals do we use to determine intelligence?

## Lesson Plan

In this lesson, students are introduced to the Turing test (along with some
background information on Alan Turing). Students are given a short snippet of
the Turing test article and the we briefly talk about it. Finally, the Turing
test is reenacted with a real ChatBot to illustrate it in real life.

### Setup

- Readings printed out
    - `computing_machinery_short.docx`
    - `computing_machinery_long.docx`
- Prompt for ChatGPT of the form:
    ```
    I am a high school teacher demonstrating the Turing test for my students. We
    are comparing chatbot output with a real human student to see if a third-party
    is able to correctly identify who is the AI and who is the human. Could you
    pretend to be a human to illustrate how the Turing test works?
    I would like you to answer specific questions that will be asked simultaneously
    to a human student. We will then compare the answers and see if we can figure
    our which are yours and which are the human's.

    Pretending to be a human high school student from Chicago who has one minute to
    type an answer in order to illustrate the Turing test, please answer the
    following question: ..."
    ```
    - Note: `claude.ai` was unwilling to pretend to be a human
- Eliza ChatBot loaded up
    - https://web.njit.edu/~ronkowit/eliza.html

### Actual Lesson

- Review
    - What did we do yesterday?
    - How do you think you might use ChatBots in other classes if your were allowed?
        - For good?
        - For bad?
    - Show game on website and git commit that led to it being published
        - https://github.com/eric-rizzi/teaching
- Who's heard of Alan Turing?
    - Why he's famous...
    - Why he died prematurely
- Read a snippet from Computing Machinery and Intelligence paper (`computing_machinery_short.docx`)
    - What is Turing trying to describe?
    - Why? -> intelligence is hard to pinpoint?
    - How could we replicate this today in class?
- Rules:
    - Volunteer to answer questions and volunteer to "decide"
    - Questions will come from other people in class to keep them engaged
    - Decider stands with their back to the class
    - Class asks a question
        - Answerer types an answers
        - Teacher types question into ChatGPT
    - After 1m, teacher reads both answers
        - "Thing A says: ..."
        - "Thing B says: ..."
    - Once Decider thinks they know who's who, makes a guess
    - Once makes a guess, explains _why_ they made decision
    - Disallow that "type" of question and try again
        - Will eventually have list of types of questions that are disallowed
            - e.g., Doesn't know the name of the teacher -> no local context q's
- Setup:
    - Make sure to pick a "fast typer" for person typing answers
    - While waiting for a human to finish response, let class ask other questions
- Go over list of types of questions and try to describe why AI struggles with each
    - Behaviorism: Watson and Pavlov
    - Of a time to try and separate consciousness from measurement
- Talk about the performance of different ChatBots over time
    - ELIZA: https://web.njit.edu/~ronkowit/eliza.html
        - One of the original "chatter bots"
        - Reportedly designers own secretary asked him for privacy after short convo
        - Shows that flaw in Turing test is the human
- Tomorrow's discussion
    - Expectations of a good discussion
        - Direct Reference to Text
        - Building and responding to others
    - EQs
        - Read through them
        - Focus on these as read/annotate tonight

### Homework

- Read `computing_machinery_long.docx` and prepare to discuss
