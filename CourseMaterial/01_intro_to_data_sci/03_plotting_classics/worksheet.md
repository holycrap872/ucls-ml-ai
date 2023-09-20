# Plotting the Classics

Today going to do self driven exercise that does three things:

1. Reads two large text documents (books) into a program
2. Breaks the books up into chapters
3. Creates various graphs of the information contained in the chapters

# Functions to Know

Below are functions/functionality you will use throughout the worksheet. Make
sure to read the code and understand what it does because you will eventually
have to use it.

## Open and Read a File

```python
path_to_file = "/bin/bash"
with open(path_to_file, "r") as file_fp:
    text = file_fp.read()

assert len(text) != 0
```

## Count Text Occurences

```python
main_str = "I wonder how many 'on's"
number_ons = main_str.count("on")

assert number_ons == 2
```

## Split a String into Pieces

```python
main_str = "This is a sentence "
split_str = main_str.split(" ")

assert split_str == ["This", "is", "a", "sentence", ""]
```

## Get a Portion of a String

```python
main_str = "racecar"
string_piece = main_str[1:6]

assert string_piece == "aceca"
```

# Goals

## Step 0

Download _The Great Gatsby_ and _Little Women_ from Schoology and put them on
your desktop.

## Step 1

Write a function to read in the text of _The Great Gatsby_ and _Little Women_.
Print out the first 100 characters of each book. Make sure you review the
"functions to know" section above.

**Q:** Based on the first 100 characters, where do each of these books come from?

## Step 2

Print out the first 100 characters of each chapter.

**Q:** What are the first three words of the last chapter in _The Great Gatsby_?

**Q:** What are the first three words in the 10th chapter in _Little Women_?

## Step 3

Create a line graph that shows the number of occurences of Tom, Daisy, and
Gatsby within each chapter.

**Q:** What do you think happens in Chapter 7?

## Step 4

Create a line graph that shows the number of occurences of Amy, Beth, Jo, Meg,
and Laurie.

**Q:** Who do you think is the main character of the book?

## Step 5

Create a scatter plot of each book with the number of characters in each chapter
on the y axis and the number of sentenes in each chapter on the x axis.

**Q:** What is the approximate average length of a sentence in each book?

**Q:** What other text format exhibits this approximate length?

## Step 6 (bonus)

Create a "cumulative" graph that shows the number of occurences of Amy, Beth,
Jo, Meg, and Laurie.

**Q:** Based on the graph, which of the sisters do you think Laurie married?
