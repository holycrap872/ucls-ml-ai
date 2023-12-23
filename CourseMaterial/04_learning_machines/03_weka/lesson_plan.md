## Essential Questions

- How can we use existing software to build classifiers
- How do existing algorithms for categorization compare with human intuition?

## Lesson Plan

### Setup

- Weka installed on necessary computers
- `segment-*` loaded onto necessary computers
- `wisconsin_breast_cancer` loaded onto necessary computers

### Actual Lesson

- Review
    - Supervised
    - Reinforcement
    - Unsupervised
    - Classifier
    - Over-fitting
    - Human vs. Machine learning
- Goal today:
    - Eventually going to implement two more machine learning algorithms before project
    - Each a different way of viewing data
        - Decision trees: Looking for cleanest cut in data
        - Bayes: Looking for most similar matches in data
        - Neural networks: Craziness/all of the above
    - Today looking at Weka, which builds classifiers for us
- Weka walkthrough
    - Show weka
    - Explore `voting_record_labeled.csv` data
        - Load it up
        - Show various graphs
        - Build classifer
            - Decision Tree
            - Select `J48` classifier
            - Walk through output
        - Explain what classifier is doing
            - Iterating through data
            - Looking for cleanest "cut"
    - How to avoid over-fitting
        - Training set vs. Test set
        - Cross validation
- Weka activity
    - Individual activity:
        - Based on: https://youtu.be/bUsPNNr6pvg?si=G9FxZsKQJe1rz2FR
        - Load `segment-challenge.arff` in explorer
        - Select `UserClassifier`
        - Use `segment-test.arff` as test set
        - See how well you can classify the data
            - J48 can do it with 96% accuracy
- Weka walkthrough 2
    - Explore `wisconsin_breast_cancer` data
    - Overall point that cancer is "abberant"
- Reflection
    - Search space metaphor
    - Decision tree metaphor

#### Homework

- Read epistomology paper

#### Resources

- https://storm.cis.fordham.edu/~gweiss/data-mining/datasets.html
- https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data?resource=download
