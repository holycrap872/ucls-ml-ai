## Essential Questions

- What practices can I adopt to make my knowledge easily viewable and sharable?

## Lesson Plan

The goal here is to move from local git to a deployed repository. Then, with
their first commit, students will create a markdown README for a `Today I Learned`
project that they will add to over time.

> Student's normal creds work (LDAP) automatically work with GitLab

### Setup

None unless you want to use a "class group". Might want them do this on the
school provided computers for some amount of sanity.

### Actual Lesson

- Review
    - `git` in comparison to GoogleDocs
    - `git` is just a bunch of diffs
    - Staged changes vs. unstaged changes
    - Do a real world example of a project as a class
        - Go SLOW!
        - Have them again do changes along with me on their git worksheet
- Today going to push `git` to the cloud
    - Show some examples in gitlab
        - Look at commits to see what's going on
    - Have everyone create their own til project in git
        - GitLab > Create New Project
            - Name: Today I learned
            - Project slug: til
            - Visibility Level: Internal
            - Initialize with README: True
    - Allow them to briefly explore effects of creating a repo via GitLab
        - Notice paths in URL
        - Notice number of commits
    - Every good project has a `README.md`
        - `README.md` is in markdown
            - Basically opposite of mark up
            - Philosphy of markdown: Structure that's as readable as possible
        - Show raw file vs. rendered file
        - Have them edit the existing README to include:
            - List of categories covered (eventually)
                - Python
                - AI
                - Git
                - Shell
            - Link to outside website
            - A License Section
    - Now going to clone
        - Pull down TIL
    - Goal today:
        - Get started on homework

### Homework

```
Create and push your first TIL entry. The entry must:

1. Be inside its own "category" folder inside your til repository
2. Have a title, a brief writeup and and example (use this as a model)
3. Be linked to in the README.md

This means that your commit will include changes to two files: the file that contains your new entry and a change to the README (to insert the link).
```
