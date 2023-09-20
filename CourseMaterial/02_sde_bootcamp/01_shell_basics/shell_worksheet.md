# Shell Worksheet

This worksheet will test your ability to use various basic commands in shell as
well as your ability to move around the file system. The sheet involves two main
parts: preparation and execution.

# Preparation

## Knowledge Transfer

Watch the following video that explains a bunch (but by no mean all) shell
commands: https://youtu.be/gd7BXuUQ91w?si=wykRpbOiXLn6gu-E&t=20 .
  - Watch the portions talking about `ls` -> `clear`
  - Watch the portions talkinga bout `curl` -> `find`
  - Watch each portion again since it goes pretty fast

## File System Setup

Download the `shell_exercise.zip` folder from Schoology. Move it do your
`Desktop` and `unzip` it.

# Execution

## Exploration

In the figure below, fill in the blank spaces with what you observe in the
`shell_exercise` folder tree.

```
~/Desktop
  /shell_exercise

    /__________________

      /_____________.txt

      /__________________.txt

      /__________________
        /file_0.txt
        /...
        /file_999.txt
```

## Investigation

1. What string does `.hidden_folder/big_file.txt` repeat over and over?
2. How many lines does `.hidden_folder/big_file.txt` contain?
3. What is the difference between `.hidden_folder/big_file.txt` and `.hidden_folder/other_big_file.txt`?
4. Looking at the man page of `cp`, what does `-r` do?

## Action

1. Make changes such that the `shell_exercise` folder structure now looks like:

```
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
```
