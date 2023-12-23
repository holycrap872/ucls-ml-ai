## Lesson Plan
- 

### Actual Lesson

- Circles that eat food
    - https://youtu.be/Sx_l2GxBC5w
- I really like this example because it's more visual than sudoku
    - Good use of classes
    - Problem is that need some amount of explanation about targetting
        - For example, can't just stop on a dime
        - That being said, a really good setup for a lot of the stuff we're doing in emergence
- Overall program
    - Random food showing up all over screen
    - Random placement of a bunch of different sized circles
        - Speed of circle inversely proportional to size
    - Circles "slowly" starve (represented by going from black to white)
        - Getting food replenishes them
    - Occassionally circle produces off spring
        - Offspring shoots off in random direction
    - Steering
        - Example I took it from just basically do random vector changes
        - To reduce the math and increase the evolutionary aspect:
            - have three cells in "DNS":
                - size / inverse speed
                - % chance of switching x direction
                - % chance of switching y direction

## Resources

- https://natureofcode.com/book/chapter-9-the-evolution-of-code/
    - "Ecosystem simulation" example

