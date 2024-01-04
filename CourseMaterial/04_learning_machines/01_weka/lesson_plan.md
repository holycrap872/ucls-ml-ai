## Essential Questions

- How can we use existing software to build classifiers
- How do existing algorithms for categorization compare with human intuition?

## Lesson Plan

### Setup

- Weka installed on necessary computers
- `wisconsin_breast_cancer` data loaded onto necessary computers

### Actual Lesson

- Review
    - Supervised
    - Reinforcement
    - Unsupervised
    - Classifier
    - Over-fitting
    - Human vs. Machine learning
- What is a classifier?
    - Give simple data and see if can come up with classifier
    - Draw decision tree for it
    - This is an example of a "classifier program"
    - Could easily implement this in python with simple if/else
- Give more complex data
    - How could we approach this
    - Graph in different ways and try and find different splits
        - Have different graphs of data along x/y axis with clear "split" somewhere
- Goals for next few weeks:
    - Eventually going to implement two more machine learning algorithms before project
    - Each a different way of viewing data
        - Decision trees: Looking for cleanest cut in data
        - Bayes: Looking for most similar matches in data
        - Neural networks: Craziness/all of the above
- Today going to use Weka
    - Program for building classifiers
    - Difficult to use, so pay attention
    - Going to build a decision tree both manually and w/ program (called `J48`)
- Weka activity
    - Based on: https://youtu.be/bUsPNNr6pvg?si=G9FxZsKQJe1rz2FR
    - Explore `wisconsin_breast_cancer` data
        - Load it up
        - Show various graphs
        - Discuss what we see in terms of decision tree
    - Build `UserClassifier`
        - Load `cancer-challenge.csv` in explorer
        - Select `UserClassifier`
        - Use `cancer-test.csv` as test set
        - See how well you can classify the data
            - `J48` can do it with ~91% accuracy
    - Build classifier using `J48` classifier
        - Walk through output
        - Compare with the decision tree we built
        - Explain what classifier is doing
            - Iterating through data
            - Looking for cleanest "cut"
- Reflection
    - What was your resulting classifier performance?
    - What is a decision tree?
    - How is a decision tree a classifier?
    - Why is a test set necessary?
    - Overall point that cancer is "abberant"

#### Homework

- None

#### Resources

- https://storm.cis.fordham.edu/~gweiss/data-mining/datasets.html
- https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data?resource=download
