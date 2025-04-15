## Essential Questions

- What is JSON and why is it so prevalent?
- How can JSON help us write more flexible programs?

## Lesson Plan

### Setup

- Solution associated with `Text Analysis Worksheet` printed out so students can analyze it
    - `text_analysis_partial.py`
- `groklearning.com` open on "student progress" tab
    - `Web Developer Tools` open
    - Student names hidden by making window small
- `EmojiPic Worksheet` posted to Schoology
    - Structured: https://docs.google.com/document/d/1nuOUKBjcMtZB4cs4miADyMmzVowSWINpeCWuurLt1sw
    - Structured: https://docs.google.com/document/d/1rEZU8kaY4DA9z7RObT1ZmhdPCIjQHulyetspzzGl2P0
    - Note: emoji_pics are already in `ProblemSetSkeleton`

### Actual Lesson

- Reflection
    - Things that were easy/hard about `Text Analysis Worksheet`?
    - Code discussion
        - Discuss
            - What was easy/hard
            - Overall structure
            - Importance of helper functions
        - Build off my version (`text_analysis_partial.py`) in class
- Today going to talk about JSON
    - In many ways the communication language of the internet
    - Allows you to send data structures between computers
- Show Grok: 
    - Go to URL: https://groklearning.com/dashboard/99895/students/#/assignments/?group=59221
        - Look in network for `student-data-batched` for student "objects"
        - Look in network for `student-assignment-data-batched/` for student progress "objects"
    - Put `student-assignment-data-batched/` in JSON formatter
        - No identifiable information
        - What do you notice/wonder?
        - Serialization and deserialization
- JSON Syntax
    - Should look very familiar
    - JSON demo where do stuff with `'{"name": "eric", "job": "teacher"}'`
        - Length of string vs. length of `json.loads()` result
        - Iterate through string vs. iterate through `json.loads()` result
        - ...
- Today going to use JSON to share pictures (EmojiPics)
    - Show EmojiPic flag and discuss what's going on
        - Need to represent 8 colors
    - Have them come up with their own file format
        - Pros and cons
        - How encode height/width?
        - What do you remember from 9th grade about this?
- Talk through my file format of EmojiPics:
    - Have `color_flag.json` and `color_flag.txt` side by side
- Today going to create an EmojiPic printer
    - Input: JSON
    - Output: EmojiPic
    - Key Functions?
        - Advanced students can skip this part
        - `bits_to_emoji()`
        - `load_dict_from_file()`
    - Where to start?
        - Advanced students can skip this part
        - What should file look like?
- Go!
    - My version at `emoji_pics/emoji_outputter.py`

### Homework

- Data structures 19 - 20
- TIL on JSON

### Possible Extensions

- Do JSON serialize/deserialize together on screen
    - JSON of scrabble words
- JSON Bingo
    - Hand out bingo cards of the form `{"B": [5, 3, 6], ...}`
    - Play manually for a round or two
    - Create a program that takes in a JSON bingo card and allows user to play
