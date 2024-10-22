## Essential Questions

## Lesson Plan

### Setup

None

### Actual Lesson

- Review
    - Libraries
    - Installing libraries
    - Show documentation for libraries
    - Monte carlo
- Functions from last class
    - `get_random_point()`
    - `is_in_circle()`
- Create program together (again)
```python
num_in_circle = 0
for trial_num in range(100):
    point = get_random_point()
    if is_in_circle(point):
        num_in_circle += 1

print(num_in_circle)
```

- Next steps
    - Graph it (circle of blue/yellow)
    - Show graph of pi over time
- Go

### Homework

- TIL entry on `random.random()`
- Python List Wheaties 11 - 13
