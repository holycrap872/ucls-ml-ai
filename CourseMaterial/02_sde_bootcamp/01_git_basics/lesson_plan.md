## Essential Questions

- What are the benefits of version controlling your software
- Why are diffs such a powerful primitive?

## Lesson Plan

The goal of this lesson is to introduce students to git. I _do not_ want them to
be git experts coming out of this. Instead, I would like them to know why git is
important and to understand in general how git is a chain of diffs. With that
foundation, we can emphasize certain aspects of git in future lessons as they
are needed. In summary, as long as they understand the "graph" concept and the
`git log` concept, then I'm happy.

### Setup

A few example git repositories to chew on.

### Actual Lesson

- Reflection from previous lesson
    - What is shell?
    - Why do we need shell?
    - Do a quick example as a class.
- What do we know about git?
    - Version control
    - Totally dominated/took over
        - Interesting history w/ Linus Torvald
    - Why do you think so popular?
- What do you notice about a real git repository?
    - https://gitlab.ucls.uchicago.edu/ml-ai/git-example
    - Have click around for 3-5 minutes
- Why git?
    - Make small changes over time
    - Track who's making changes
    - Easily go back in history
    - GitHub!
        - Git was designed for collaboration
    - Philosophical changes caused by GitHub
        - Open source movement on steroids
            - Pull/merge requests
            - Forks
- Essence of git
    - Diffs!
    - Show example diffs from shell exercise
    - Draw as a network/graph
    - Show equivalent in git: https://gitlab.ucls.uchicago.edu/ml-ai/git-example
- What is going on under the hood
    - Staging area -> makes for pretty commits
    - Do a word ladder as a class
        - Have do changes along with me on their git worksheet
            - Inspired by https://software-carpentry.org/blog/2018/05/git-worksheets.html
- Show them some of class's repos
    - https://gitlab.ucls.uchicago.edu/ml-ai/problem-set-skeleton

### Homework

- Create a TIL repository
    - Create github account
    - create repository named "til"
    - Add an entry to til
    - Good example: https://github.com/jbranchaud/til
- Create a 5 word sentence "ladder"
    - Put each word on its own line
    - Go from one sentence to a completely new sentence with one line changes
    - Each change gets its own commit
    - Represent this as git would
- Clone our classes "Problem Set Skeleton" and do problem set lists in it?

### Resources
- https://youtu.be/8JJ101D3knE
    - Good general introduction up to minute 6
    - Make clear get bonus points (fake) if can do it on command-line
- https://youtu.be/i_23KUAEtUM
    - Git for vscode
    - Kind of relies on you knowing git/purpose of git
    - Not sure how much git knowledge people have
