## Essential Questions

- What practices can I adopt to make my knowledge easily viewable and sharable?

## Lesson Plan

The goal here is to show students how git can go from a "local" repository to a
"remote" repository. To do this, students will build on (and push) a "Today I
Learned" skeleton. This project will then be something that they add to over
time.

> Student's normal creds work (LDAP) automatically work with GitLab

### Setup

- TIL skeleton zipped loaded onto Schoology
    - Taken from `https://gitlab.ucls.uchicago.edu/ml-ai/til`
    - `.git` folder removed
- Maybe use a "class group"?
- Maybe do this on school provided computers for some amount of sanity?

### Actual Lesson

- Review
    - `git` in comparison to GoogleDocs
    - `git` is just a bunch of diffs
    - Staged changes vs. unstaged changes
    - Do a real world example of a project as a class
        - Go SLOW!
        - Have them again do changes along with me on their git worksheet
- Today going to create long-running "knowledge tracker"
    - Uses git
    - Will push repository to cloud so can't be lost
- Show inspiration
    - https://github.com/jbranchaud/til
    - Walk through various things
    - How is GitLab similar to GitHub?
- Show some examples in gitlab
    - https://gitlab.ucls.uchicago.edu/vdangi/til
    - Look at commits to see what's going on
- Have everyone create their own til project in git
    - GitLab > Create New Project
        - Name: Today I learned
        - Project slug: til
        - Visibility Level: Internal
        - Initialize with README: False
    - Download skeleton from Schoology
    - Push
- Every good project has a `README.md`
    - `README.md` is in markdown
        - Basically opposite of mark up
        - Philosophy of markdown: Structure that's as readable as possible
    - Show raw file vs. rendered file
- Have them edit the existing README to include:
    - List of categories covered (eventually)
        - Python
        - AI
        - Git
        - Shell
    - Link to outside website
    - A License Section
- Get started
    - Create content on markdown "viewer"
        - https://markdownlivepreview.com/
    - Open TIL skeleton
    - Paste in entry
    - Push
- Goal today:
    - Get started on homework

### Homework

```
Create and push your first TIL entry. The entry must:

1. Be inside its own "category" folder inside your til repository
2. Have a title, a brief writeup, and an example
3. Be linked to in the `README.md`

This means that your commit will include changes to two files: the file that
contains your new entry and a change to the `README.md` (to insert the link).
```
