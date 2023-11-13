# Markov Chain Text Generation

Markov chains are a way of modeling a memoryless system. While not nearly as
accurate as other techniques for text generation that can store context (e.g.,
Neural Networks), they can still lead to some very interesting results.

The data that we will be operating on will come from the Project Gutenberg books
that we used in our previous lesson.

## Model Modeling

We're going to start with a simple, contrived example. Assume we are going to
ingest a book whose contents are: "Fish swim, fish jump; I swim, I fish".

1. In the space below, show the dictionary that represents the "Markov graph"
   of this sentence (including the implied "^" and "$").
    ```
    {
        "^":    {                              },
        "fish": {                              },
        "swim": {                              },
        "jump": {                              },
        "i":    {                              }
    }
    ```
2. Using this model, what is a sentence that could be generated starting with "i"?

## Model creation

Now we're going to operate on real data. Choose _one_ of your books from your
`data` folder. Make sure that and _any pre/post text_ that has to do with
Project Gutenberg has been removed.

1. For generating the "Markov graph" associated with the book:
    - What book did you choose?
    - Including types, what data structure should you use?
    - What are three functions you could create that will make implementation easier?
        - Function 1:
        - Function 2:
        - Function 3:
    - Implement functionality to calculate it!
2. Looking at the model/graph you just generated:
    - What word most commonly follows "and"?
    - What word has the greatest number of words that follow it?
    - How many total transitions (word -> word) are there?
    - What is the most common word -> word transition?

## Most Common Sentence

Now we're going to use the model/graph to generate some sentences. In this part
of the exercise, we're going to follow the "most likely" transition every time.
This means we **don't yet need** to use any call to `random`.

1. For generating the "most common sentence" of **a given length**:
    - What are two functions you could create that will make implementation easier?
        - Function 1:
        - Function 2:
    - Implement functionality to calculate it!
2. What is the "most common sentence" eight-word sentence that starts with "i"?
    ```
    ```
3. What is the "most common sentence" eight-word sentence that starts with a word of your choosing?
    ```
    ```

## Most Common Non-Repeating Sentence

The output above was likely a bit unimpressive. To make it a little more
realistic, we are going to add a "non-repeating" constrain to our sentence
generator. To do this, add/use a CONST variable named `SAID_WORDS`. Figure out
how to use this to prevent the same word from being output more than once.

1. For generating the "most common, non-repeating sentence" of **a given length**:
    - What is the function you will need to alter?
    - Implement functionality to calculate it!
2. What is the "most common sentence" eight-word sentence that starts with "i"?
    ```
    ```

## True Markov Chain Generation

Now we're going to get `random`. In this part of the exercise, the probability
that we follow a transition is proportional to the number of occurrences it has.

1. For generating a "true Markov-chain generated sentence" of **a given length**:
    - What is the function you will need to alter?
    - Implement functionality to calculate it!
2. What is a Markov chain generated eight-word sentence that starts with "i"?
3. Ingest a different book from the one you've been using up to this point.
    - What is a Markov chain generated eight-word sentence that your program produces given this input?
        ```
        ```
4. Ingest four different books at the same time.
    - What is a Markov chain generated eight-word sentence that your program produces given this input?
        ```
        ```

## Markov Chain Visualization

You can output a simple visualization of a graph using the following snippet of
code:

```python
import matplotlib.pyplot as plt
import networkx as nx

def visualize() -> None:
    graph = nx.DiGraph()

    # Add nodes (you can also add nodes along with the edges)
    graph.add_nodes_from(["the", "person", "ate"])

    # Add edges with weights (representing transition probabilities)
    graph.add_edge("the", "person", prob=0.6)
    graph.add_edge("person", "ate", prob=0.4)

    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_edges(graph, pos, edgelist=graph.edges(), arrowsize=30)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(graph, "prob"))

    plt.show()
```

Use this example to create a function that outputs a visualization of the
Markov chain your program creates. Test it by ingesting the sentence "Fish swim,
fish jump; I swim, I fish".
