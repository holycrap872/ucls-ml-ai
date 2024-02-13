## Essential Questions

-

## Lesson Plan

### Setup

- Machine code worksheet printed out
- CPU and memory as wrap up

### Actual Lesson

- Review
    - Learned about machine code
    - What were some operations we learned about
        - add
        - jmp
        - set memory
- How to view computer
    - Huge list of 64 bit slots
    - Filled with instructions and data
    - Instructions explain how to operate on data
- Real world example
    - Compile simple program
        - `gcc -masm=intel -arch x86_64 -O0 -o simple simple.c`
            - Cross compiling for readability
        - `objdump -D simple > out.dump`
        - Show how `for` loop is changed into a `jmp`
- Show simple machine code program and have figure out what it's doing
    - simple for loop that goes up to 10 and returns value
    - simple if/else
- Most programs work this way-ish
    - Allocate space for variables
    - Compiler turns code that's human reasonable to code that machine runnable
- How would primitives be represented?
    - Single slot
    - What's the problem with lists/sets/maps

- Worksheet
    - "Compile" simple programs I give you
    - Look at a Human Resource thing and program in python and program in machine code
- The annoyance of functions
    - Lists

- Little man computer
    - https://peterhigginson.co.uk/LMC/?F5=07-Feb-24_03:39:25