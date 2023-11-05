## Essential Questions

- What is json and why is it so prevalent?
- How can json help us write more flexible programs?

## Lesson Plan

#### Day 1

- Reflection
    - Things that were easy/hard about the text analysis
    - Show my Jaccardian analysis
    - Role of data in the text analysis
        - What if you didn't remove the Project Gutenberg header/footer?
        - What if you didn't use different authors?
        - How could we make it more accurate?
- Today going to talk about JSON
    - In many ways the communication language of the internet
- Show grok: 
    - Go to URL: https://groklearning.com/dashboard/99895/students/#/assignments/?group=59221
        - Look in network for `student-data-batched` for student "objects"
        - Look in network for `student-assignment-data-batched/` for student progress "objects"
    - Put in json formatter
        - What do you notice/wonder?
- JSON Demo
    ```python
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
- Theory of JSON:
    - Why is it so prevelent?
    - Where are the sets?
- Talk through emoji pics:
    - Talk through file format
        - Have flag.json and pic side by side
    - Key Functions
        - encoding_to_emoji()
        - load_dict_from_file()
- Go!
    - `color_outputter.py`

#### Day 2

- Review
    - JSON
    - Show someone's TIL entry and discuss
- JSON serialization/deserialization
    - How would I output json another thing can use
    - Show can't just print out a dictionary
    - Dumps
    - Verify correct using a json formatter
        - What language is json formatter in?
        - Doesn't matter... language agnostic
- Emoji Outputter
    - Review
    - Come up with key functions
- Go!

### Homework

- Data structures 13-14 (only b/c I don't see them until Monday)
- TIL on JSON

### Potential Extensions

- Do JSON encode/decode together on screen
    - JSON of scrabble words