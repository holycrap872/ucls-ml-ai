1. Select the **four** capabilities the `list` data structure has:
- Getting the first element via `list[0]`
- Getting the length via `len(list)`
- Iterating through the items via `for elem in list:`
- Determining if the list has an element via `elem in list`
- QUICKLY determining if the list has an element via `elem in list`
- Getting the data related to an element via `list[elem]`

2. Select the **four** capabilities the `set` data structure has:
- Same options as above

3. Select the **five** capabilities the `dict` data structure has:
- Same options as above

4. Which data structure would best represent the following situation: The id numbers of racers as they finish a race.
- list[int]
- list[str]
- set[int]
- set[str]
- dict[str, int]
- dict[str, str]

5. Which data structure would best represent the following situation: The countries that have ever won the World Cup.
- Same options as above

6. Which data structure would best represent the following situation: The capital of every state.
- Same options as above

7. How might a student named Cecily Strong who lives at 123 Main Street be stored in a database:
- A function of the form: `get_data(first_name: str, last_name: str, address: str):`
- A list of the form: `["first_name", "Cecily", "last_name", "Strong", "address", "123 Main Street"]`
- A dict of the form: `{"first_name": "Cecily", "last_name": "Strong", "address": "123 Main Street"}`
- A set of the form: `{"Cecily", "Strong", "123 Main Street"}`

8. What will be the output of the following code:
    ```python
    x = {1, 2, 4, 2, 1}
    v1 = len(x)
    x.add(6)
    v2 = len(x)
    x.add(4)
    v3 = len(x)
    print(v1, v2, v3)
    ```

9. What will be the output of the following code:
    ```python
    x = [1, 2, 4, 2, 1]
    v1 = len(x)
    x.append(6)
    v2 = len(x)
    x.append(4)
    v3 = len(x)
    print(v1, v2, v3)
    ```

10. What will be the output of the following code:
    ```python
    x = {"hey": 3, "there": 5}
    v1 = len(x)
    x["you"] = 3
    v2 = len(x)
    x["hey"] = 4
    v3 = len(x)
    v4 = x["hey"]
    print(v1, v2, v3, v4)
    ```
