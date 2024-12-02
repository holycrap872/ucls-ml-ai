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
- `emoji_pics.zip` loaded up in Schoology
    - `pic_0.json`: `color_flag.json`
    - `pic_1.json`: `color_mario.json`
    - `pic_2.json`: `color_turkey.json`
    - `pic_3.json`: `color_whale.json`
- `EmojiPic Worksheet` posted to Schoology
    - Structured: https://docs.google.com/document/d/1nuOUKBjcMtZB4cs4miADyMmzVowSWINpeCWuurLt1sw
    - Structured: https://docs.google.com/document/d/1rEZU8kaY4DA9z7RObT1ZmhdPCIjQHulyetspzzGl2P0

### Actual Lesson

- Reflection
    - Things that were easy/hard about `Text Analysis Worksheet`?
    - Role of data in the analysis
        - What if you didn't remove the Project Gutenberg header/footer?
        - What if you didn't use different authors?
        - How could we make it more accurate?
- Code discussion
    - Discuss
        - What was easy/hard
        - Overall structure
        - Importance of helper functions
    - Build off my version (`text_analysis_partial.py`) in class
- Today going to talk about JSON
    - In many ways the communication language of the internet
    - Way to send data structures between computers
        - 1/0 -> Numbers (via binary)
        - Numbers -> Letters (via ASCII)
        - Letters -> Data structures (via JSON)
- Show Grok: 
    - Go to URL: https://groklearning.com/dashboard/99895/students/#/assignments/?group=59221
        - Look in network for `student-data-batched` for student "objects"
        - Look in network for `student-assignment-data-batched/` for student progress "objects"
    - Put `student-assignment-data-batched/` in JSON formatter
        - No identifiable information
        - What do you notice/wonder?
        - Serialization and deserialization
- Theory of JSON:
    - Why is it so prevalent?
        - Allows computers to share complex information
    - Where are the sets?
- JSON Demo
    ```python
    import json

    def json_demo() -> None:
        received_json_dict_via_internet = '{"name": "eric", "job": "teacher"}'

        # print(received_json_dict_via_internet["name"])  WILL FAIL
        # print(received_json_dict_via_internet["job"])  WILL FAIL
        print(len(received_json_dict_via_internet))
        # print(received_json_dict_via_internet["no_key"])  WILL FAIL

        dict_2 = json.loads(received_json_dict_via_internet)

        print(dict_2["name"])
        print(dict_2["job"])
        print(len(dict_2))
        print(dict_2["no_key"])

    if __name__ == "__main__":
        json_demo()
    ```
- Today going to use JSON to share pictures (EmojiPics)
    - Show EmojiPic flag and discuss what's going on
        - Need to represent 8 colors
    - Have them come up with their own file format
        - Pros and cons
        - How encode height/width?
        - What do you remember from 9th grade about this?
- Talk through my implementation of EmojiPics:
    - Talk through file format
        - Have `color_flag.json` and `color_flag.txt` side by side
- Today going to create an EmojiPic printer
    - Input: JSON
    - Output: EmojiPic
    - Key Functions?
        - Advanced students can skip this part
        - encoding_to_emoji()
        - load_dict_from_file()
    - Where to start?
        - Advanced students can skip this part
        - What should file look like?
- Go!
    - My version at `emoji_pics/emoji_outputter.py`

### Homework

- Data structures 19 - 20
- TIL on JSON

### Potential Extensions

- Do JSON serialize/deserialize together on screen
    - JSON of scrabble words
- JSON Bingo
    - Hand out bingo cards of the form `{"B": [5, 3, 6], ...}`
    - Play manually for a round or two
    - Create a program that takes in a JSON bingo card and allows user to play
