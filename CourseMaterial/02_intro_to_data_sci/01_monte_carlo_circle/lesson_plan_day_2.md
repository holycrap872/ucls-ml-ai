## Essential Questions

- How can we use randomness to solve hard problems?
- How does the quantity and quality of data affect ML outcomes?

## Lesson Plan

### Setup

- None

### Actual Lesson

- Review
    - Libraries
    - Installing libraries
    - Show documentation for libraries
    - Monte carlo
- Functions from last class
    - `distance_from_origin()`
    - `is_in_circle()`
- Create program together (again)
    ```python
    num_in_circle = 0
    for trial_num in range(100):
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1
        if is_in_circle(x, y):
            num_in_circle += 1

    print(num_in_circle)
    ```

- Next steps
    - Graph it (circle of blue/yellow)
    - Show graph of pi over time
- Go

### Homework

- `Python List Wheaties` 11 - 13
