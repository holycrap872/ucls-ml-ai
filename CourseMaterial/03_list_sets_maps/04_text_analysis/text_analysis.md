# Comparing Books Over Time

The way that people communicate changes over time. This includes the words
that they actually use. In this exercise, we are going to investigate the
similarities and differences in language over decades.

The data that we will be operating on will come from Project Gutenberg. First,
choose two non-consecutive decades (1920's or before for copyright reasons).
Then, go to https://www.goodreads.com/list/show/39 and find two books from
different authors from each of those decades and verify that they are available
on Project Gutenberg.

1. Decade 1: _______________
    - Book 1: _______________
    - Book 2: _______________
2. Decade 2: _______________
    - Book 3: _______________
    - Book 4: _______________

## Single book statistics

We're going to start our exploration with Book 1. Download it and place it in
a `data` folder (or something similar). _Remove any pre/post text_ that has to do
with Project Gutenberg.

1. For calculating the number of **total words** in the book:
    - What data structure should you use?
    - Implement functionality to calculate it!
    - How many total words are in the book?
2. For calculating the number of **unique words** in the book:
    - What data structure should you use?
    - Implement functionality to calculate it!
    - How many unique words are in the book?
3. For counting the number of times each word appears in the book:
    - What data structure should you use?
    - Implement it!
    - How often does the word `"and"` appear in the book?
    - What is the most common word in the book and how often does it occur? 
    - What are two or three words that only occur once?
4. Print out all of the words that occur only once in the book:
    - What are two or three of them?
    - Is there anything you can do to clean up your data?
        - Call Mr. Rizzi over for a quick discussion.

## Book to book comparison

Load up the other book **from the same decade** as the one you analyzed in the
previous section.

1. Is the word `"and"` in both books?
2. For calculating the words that appear in at least one of the books (aka in **either** book):
    - What data structure should you use?
    - Draw a Venn diagram of what portion you want to select:
        ```






        ```
    - Implement functionality to calculate it!
    - How many unique words are in at least one of the books?
3. For calculating the words that the books have in common (aka in **both** books):
    - What data structure should you use?
    - Draw a Venn diagram of what portion you want to select:
        ```






        ```
    - Implement functionality to calculate it!
    - How many unique words are in both of the books?
4. For calculating the words that are only in the first book and not the second:
    - What data structure should you use?
    - Draw a Venn diagram of what portion you want to select:
        ```






        ```
    - Implement functionality to calculate it!
    - How many unique words are only in the first book?
    - What are two or three of these words?
5. How many times does the most common word in the first book appear in the second?

## Decade to decade comparison

Load up the two books from the decade that we haven't analyzed yet.

Create a set of words that are _in both books_ from your first decade and a set
of words that are _in both_ books from your second decade.

1. For calculating what words are only in the books from the **first decade**:
    - What set operation should you use?
    - Implement functionality to calculate it!
    - How many words are only in the books from the first decade?
    - What are two or three of these words?
    - Give a one sentence explanation of what this set represents:
2. For calculating what words are only in the books from the **second decade**:
    - What set operation should you use?
    - Implement functionality to calculate it!
    - How many words are only in the books from the second decade?
    - What are two or three of these words?
    - Give a one sentence explanation of what this set represents:

## Estimation via Jaccard Similarity

In this final section, we're going to try and guess what decade a random book
is from. First, watch the following video on Jaccard similarity:
https://youtu.be/YotbvhndSf4?si=nqIJlZwylLw8keG7 .

1. What does Jaccard similarity attempt to measure?
2. Have a partner pick a random book from one of your two decades:
    - What is the "Jaccard similarity" of the random book with the books from
      your first decade?
    - What is the "Jaccard similarity" of the random book with the books from
      your second decade?
    - Based on these numbers, which decade is it more likely the book is from?
    - Were the results true? Why or why not?
