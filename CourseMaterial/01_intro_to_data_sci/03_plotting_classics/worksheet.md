# Plotting the Classics

Today we are going to do a self driven exercise that does three things:

1. Reads two large text documents (books) into a program
2. Breaks the books up into chapters
3. Creates various graphs of the information contained in the chapters

# Functions to Know

Below are functions/functionality you will use throughout the worksheet. Make
sure to read the code and understand what it does because you will eventually
have to utilize each piece.

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

# Setup

Download _The Great Gatsby_ and _Little Women_ from Schoology and put them on
your desktop.

# Exploring (with the python interpreter in Terminal)

## Step 1

Read in the text of _The Great Gatsby_ and _Little Women_ into your program.

**Q:** How many characters are in each book?

**Q:** Print out the first 100 characters of each book. Based on this text, where
       do each of these books come from?

**Q:** Looking at the text, what is a good substring to `split()` the text into chapters?

**Q:** What will be returned by the `split()` operation?

**Q:** What are the first ten characters of the second chapter of _Little Women_?

## Step 2

Focus on the text of _The Great Gatsby_.

**Q:** Looking at the chapters, what is a good substring to `split()` the text
       into individual words?

**Q:** What will be returned by the `split()` operation?

**Q:** What are the *first three words* of the last chapter in _The Great Gatsby_?

**Q:** What are the *last three words* in the third chapter in _The Great Gatsby_?

**Q:** How often does the word "Gatsby" show up in the entire Great Gatsby text?

**Q:** How often does the word "Gatsby" show up in the second chapter?

# Programming (write actual functions in python)

## Step 1

Create a line graph that shows the number of occurences of "Tom", "Daisy", and
"Gatsby" within each chapter.

**Q:** What do you think happens in Chapter 7 and why?

## Step 2

Create a line graph that shows the number of occurences of "Amy", "Beth", "Jo",
"Meg", and "Laurie" within each chapter.

**Q:** Who do you think is the main character of the book?

## Step 3

Create a scatter plot of each book with the number of characters in each chapter
on the y-axis and the number of sentences in each chapter on the x-axis.

**Q:** What is the approximate average length of a sentence in each book?

## Step 4 (bonus)

Create a graph that shows the cumulative number of occurences of "Amy", "Beth",
"Jo", "Meg", and "Laurie" throughout each chapter.

**Q:** Based on the graph, which of the sisters do you think Laurie married?
