## Essential Questions

- Where does consciousness lie?
- What signals do we use to determine intelligence?

## Lesson Plan

In this lesson, students are introduced to the Turing Test (along with some
background information on Alan Turing). Students are given a short snipped of
the Turing Test article and a brief discussion is had. Finally, the Turing Test
is enacted with a real ChatBot to really drive the point home.

### Setup

- Ear plugs/muffs to dampen sound
- Readings printed out
    - `turing_paper_snippet.md`
    - `shortened_article_20m`
- Connection to Claude.ai
    - **Clear our any old history** for both ChatGPT and Claude
    - Prompt for Claude.ai of the form:
```
I am trying to use Malcolm Gladwell's talk "On Spaghetti Sauce" to understand
how search spaces and search space exploration work. Could you create a medium
length paragraph answering the question "what mistake did Prego make in terms of
their objective function when trying to find the perfect spaghetti sauce"?
```
    - Prompt for Claude.ai of the form:
```
I am a high school teacher demonstrating the Turing Test for my students. We
are comparing chatbot output with a real human student to see if a third-party
is able to correctly identify who is the AI and who is the human. Could you
pretend to be a human to illustrate how the Turing Test works?

I would like you to answer specific questions that will be asked simultaneously
to a human student. We will then compare the answers and see if we can figure
our which are yours and which are the human's.

Pretending to be a human high school student from Chicago who has one minute to
type an answer in order to illustrate the Turing Test, please answer the
following question: ..."
```

### Actual Lesson

- Refresher
    - What did we do yesterday?
    - What do **parameters** mean?
    - What is an **object function** mean?
    - What is a local maxima?
    - What is max gradient ascent?
    - How does "growing the perfect sunflower" map onto this?
- Claude.ai intro
    - Look at the homework
    - We know Claude.ai is good at this kind of thing, so let's see what it says
        - Ask question on homework of Claude.ai
    - Today, going to see how smart Claude.ai is
- Who's heard of Alan Turing?
    - Why he's famous...
    - Why he died prematurely
- Read a snippet from the paper (`turing_paper_snippet.md`)
    - What is Turing trying to describe?
    - Why? -> intelligence is hard to pinpoint?
    - How could we do this today in class?
- Rules:
    - Volunteer to ask questions and volunteer to answer
    - Questioner stands with their back to the class with ear plugs/muffs on
    - Questioner asks a question
        - Answerer answers
        - Teacher types question into Claude.ai
    - After 1m, teacher reads both answers
        - "Thing A says: ..."
        - "Thing B says: ..."
    - Once questioner thinks they know who's who, makes a guess
    - Once makes a guess, explains _why_ they made decision
    - Disallow that "type" of question and try again
        - Will eventually have list of types of questions that are disallowed
            - e.g., Doesn't know the name of the teacher -> no local context q's
- Go over list of types of questions and try to describe why AI struggles with each

### Extensions (if have time)

- Talk about the performance of different chat bots over time
    - ELIZA: https://web.njit.edu/~ronkowit/eliza.html
- Discuss chatbot policy (if have time)
    - Exploratory committee about what policy the school should have
    - Likely going to ask you folks to be involved in some way to get student's view

### Homework

- Read `shortened_article_20m.md` and prepare to discuss
