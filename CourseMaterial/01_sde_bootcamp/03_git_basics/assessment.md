0. Match the following shell commands with their effects:
    - `touch hello`: Creates a new, empty file named `hello`
    - `mkdir hello`: Creates a new, empty folder named `hello`
    - `cd hello`: Moves to be inside the folder `hello`
    - `cd ..`: Moves to the "parent directory" of the current folder
    - `cp hello bye`: Copies a file named `hello` into a file named `bye`
    - `mv hello bye`: Renames a file named `hello` to a file named `bye`
    - `cd ~`: Moves to the user's "home" directory
    - `cd ../..`: Moves to the "grandparent directory" of the current folder
    - `ls`: Lists the contents of the current directory
    - `ls hello`: Lists the contents of the folder names `hello`
    - `rm hello`: Deletes the file named `hello`
    - `rm -rf /`: Deletes everything on the computer from the root down
1. Which of the following commands would turn the "folder structure" on the left
   into the "folder structure" on the right? Note that the red arrow represents
   your "present working directory"
    - ```
      > mkdir ../Desktop/example
      > cd ../Desktop/example
      > touch new_file.txt
      ```
    - ```
      > cd ../Desktop
      > mkdir example
      > touch new_file.txt
      ```
    - ```
      > touch ../Desktop/example/new_file.txt
      > cd ../Desktop/example
      ```
    - ```
      > cd ~/Desktop/example
      > touch new_file.txt
      ```
2. Which of the following commands would turn the "folder structure" on the left
   into the "folder structure" on the right? Note that the red arrow represents
   your "present working directory"
    - ```
      > mkdir ../Desktop/example
      > cd ~/Desktop/../Desktop/example
      > touch ~/Documents/new_file.txt
      ```
    - ```
      > cd ../Desktop
      > mkdir example
      > touch ~/new_file.txt
      ```
    - ```
      > mkdir ../Desktop/example
      > cd ~/Desktop
      > touch ~/new_file.txt
      ```
    - ```
      > cd ~
      > mkdir Desktop/example
      > touch Documents/new_file.txt
      > cd Desktop/example
      ```
3. `git` is an example of a program that does:
    - Version control
    - Directory management
    - Number calculations
    - Command and control
4. Match the following `git` commands with their effects:
    - `git init`: Creates a new git repository
    - `git status`: Shows the current state of the repository
    - `git add`: Stages the changes in a file
    - `git commit -m`: Commits any staged changes
    - `git diff`: Shows all untracked changes
    - `git log`: Shows the commit history of a repository
5. Under what situations would you expect to run the command `git init`?
    - Just in the beginning of a new project
    - Every time a file is changed
    - Whenever you want to remember something
    - When you want to see the state of the project
6. Under what situations would you expect to run the command `git status`?
    - Whenever you want to see which files have been changed since the last commit
    - Only once at the beginning of the project to properly set the status of the repository
    - Whenever you want to see the past commits you made to the project
    - Infrequently and only when you need to show the teacher you are working
7. Under what situations would you expect to run the command `git add`?
    - When you are happy with the changes in a file and are ready to stage them
    - When you want to see the state of the files in the repository
    - Only once when you want to turn a folder into a git repository
    - At the beginning of each day to prepare for any changes you might make
8. Under what situations would you expect to run the command `git commit`?
    - When you are happy with the changes that have been staged and want to commit them
    - Once at the beginning when you want to commit all the files to the repository's memory
    - Towards the end of a project to get everything ready for turning in the entire project
    - Whenever a file needs to be reset back to its original value
9. In the picture below, we are in a repository called `git_example`. What is the state of the `file_2.txt` file?
    - Untracked: It's hasn't yet been added to the repository
    - Tracked and Staged: It has changes but those changes haven't been committed
    - Tracked but not Staged: It has changes but those changes haven't been staged
    - Committed: The files changes have been committed to the repository in commit #41371ac
10. In the picture below, we are in a repository called `git_example`. What is the state of the `file_2.txt` file?
    - Tracked and Staged: It has changes but those changes haven't been committed
    - Untracked: It's hasn't yet been added to the repository
    - Tracked but not Staged: It has changes but those changes haven't been staged
    - Committed: The files changes have been committed to the repository in commit #41371ac
11. In the picture below, we are in a repository called `git_example`. What is the state of the `file_2.txt` file?
    - Tracked but not Staged: It has changes but those changes haven't been staged
    - Tracked and Staged: It has changes but those changes haven't been committed
    - Untracked: It hasn't yet been added to the repository
    - Committed: The files changes have been committed to the repository in commit #41371ac
12. What command would result in the output seen in the picture below:
    - `git log`
    - `git status`
    - `git diff`
    - `git commit`
    - `git add`
    - `git lg2`
13. Based on the the results of `git log` shown in the picture below
    - That the first commit had the message "Initial commit"
    - That the most recent commit was a bug fix
    - That the various commits made to the repository took more than three hours
    - That the second to last commit had a reference number #e61d0df
    - That the third to last commit had a reference number #19a774a