## Essential Questions

- What does it mean for a machine to learn?
- What are the core machine learning techniques?
- Where are each of these techniques most effective?

## Lesson Plan

### Setup

- Weka installed
- Weka's `userClassifer` plugin installed
- `segment-test.arff` and `segment-challenge.arff` in Schoology

### Actual Lesson

#### Day 1

- Going to enter brief section on "Philosophy of Learning"
- Learning unit will be two parts:
    - Given a specific type of problem, how do we best teach machines?
    - Given a specific type of problem, how do we best teach humans?
- What do we know about machine learning?
    - Data and stats
- Three basic types of learning:
    - Supervised
    - Reinforcement
    - Unsupervised
- Supervised:
    - https://studio.code.org/s/oceans/lessons/1/levels/2
    - Go through lesson 6
    - Silly, but gets the point across
- Debrief supervised
    - Labeled/Tagged data
- Reinforcement
    - Pokemon game:
        - https://youtu.be/DcYLT37ImBY?si=PUazEpIJsm2kLfhU
        - 0:00 - 3:30
    - Tons of videos on youtube like this
- Debrief reinforcement
    - Formula/function
    - Akin to evolution
- Unsupervised
    - K-means clustering
    - Somethings here... up to the expert
- Continuum of effort:
    - Supervised high human effort, unsupervised low effort
- Handling data
    - Overfitting
- Name that learning style:
    - Weather prediction -> Supervised
    - Evolution -> Reinforcement
    - Captchas -> Supervised
    - Rubrics -> Reinforcement
    - Journaling -> Unsupervised
    - Handwriting recognition -> Supervised
    - LLMs -> Unsupervised
    - Credit checks -> Supervised
- Vocab words:
    - Machine learning
    - Supervised learning
    - Unsupervised learning
    - Reinforcement learning
    - Labeled data
    - Overfitting
    - Classifier
    - Agent
    - Clusters
    - Training Set
    - Test Set

#### Day 2:

- Review
    - Supervised
    - Reinforcement
    - Unsupervised
- Weka activity
    - Show weka
    - Explore `voting_record_labeled.csv` data
        - Load it up
        - Show various graphs
        - Build classifer
        - Explain what classifier is doing
    - Individual activity:
        - Based on: https://youtu.be/bUsPNNr6pvg?si=G9FxZsKQJe1rz2FR
        - Load `segment-challenge.arff` in explorer
            - From https://storm.cis.fordham.edu/~gweiss/data-mining/datasets.html
        - Select `UserClassifier`
        - Use `segment-test.arff` as test set
        - See how well you can classify the data
    - Reflection

#### Homework

- Read `science_of_learning.docx` and prepare for discussion

### Resources:

- https://youtu.be/i_LwzRVP7bg?si=obrRe2vHGKaXYK3K&t=634
- Build your own classifier via a GUI
    - https://youtu.be/bUsPNNr6pvg?si=G9FxZsKQJe1rz2FR