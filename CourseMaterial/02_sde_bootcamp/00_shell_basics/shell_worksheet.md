# Shell Worksheet

This worksheet will test your ability to use various basic commands in shell as
well as your ability to move around the file system. The sheet involves two main
parts: preparation and execution.

# Preparation

## 1. Knowledge Transfer

Watch the following video that explains a bunch (but by no means all) shell
commands: https://youtu.be/gd7BXuUQ91w .
  - Watch the portions talking about `ls` -> `clear`
    - Look in "About Video" to find links to jump to the right part of the video
  - Watch the portions talking about `curl` -> `find`
  - Watch each portion again since it goes pretty fast

## 2. File System Setup

Download the `shell_exercise.zip` folder from Schoology. Move it do your
`Desktop` and `unzip` it.

## 3. Terminal Startup

Open up the terminal (`Applications/Utilities/Terminal`) and navigate to your
desktop (in unix: `cd ~/Desktop`). Then, go into the `shell_exercise` folder.

## 4. Chat Model Setup

Open up Bard or ChatGPT and be prepared to type any questions you might have
about shell/terminal into it.

# Execution

## 1. Exploration

In the figure below, fill in the blank spaces with what you observe in the
`shell_exercise` folder tree.

```shell
~/Desktop
    /shell_exercise

        /__________________

            /__________________.txt

            /__________________.txt

            /__________________
                /file_0.txt
                /...
                /file_999.txt
            /__________________
                /cs_quotes_v0.md
                /...
                /cs_quotes_v4.md
```

## 2. Investigation

**Q:** What was the most recently created folder?

**Q:** What string does `.hidden_folder/big_file.txt` repeat over and over?

**Q:** How many lines does `.hidden_folder/big_file.txt` contain?

**Q:** What is the difference between `.hidden_folder/big_file.txt` and
    `.hidden_folder/other_big_file.txt`?

**Q:** Looking at the man page of `cp`, what does `-R` do?

## 3. Action

1. Make changes such that the `shell_exercise` folder structure now looks like:

```shell
~/Desktop
    /shell_exercise
        /.hidden_folder
            /buncha_orig_files
                /file_0.txt
                /...
                /file_999.txt
        /visible_folder
            /big_file.txt           # hint: `mv`
            /empty_file.txt         # hint: `touch`
            /buncha_copied_files    # hint: `cp`
                /file_0.txt
                /...
                /file_999.txt
            /buncha_versions
                /cs_quotes_v0.md
                /...
                /cs_quotes_v4.md
```

# Extension

## Mild

See how far you can get in https://cmdchallenge.com

## Spicy

See how far you can get in https://overthewire.org/wargames . To get started,
you will need to "ssh" into a demonstration computer using the following
command:

```
ssh -p 2220 bandit0@bandit.labs.overthewire.org
```

> This is a _difficult_ demo and requires careful reading, but you will learn A LOT
