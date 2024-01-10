#!/usr/bin/env python3

"""
Java Equivalent:

```
import java.util.HashMap;
import java.util.Map;

interface Operation {
    int operate(int x, int y);
}

class Add implements Operation {
    @Override
    public int operate(int x, int y) {
        return x + y;
    }
}

class Subtract implements Operation {
    @Override
    public int operate(int x, int y) {
        return x - y;
    }
}

class Calculator {
    public static void main(String[] args) {
        Map<String, Operation> operationMap = new HashMap<>();
        operationMap.put("add", new Add());
        operationMap.put("subtract", new Subtract());

        int num1 = 5;
        int num2 = 4;
        String operation = "add";

        Operation op = operationMap.get(operation);
        if (op != null) {
            System.out.println("Result: " + op.operate(num1, num2));
        } else {
            System.out.println("Invalid operation");
        }
    }
}
```
"""


def add(x: int, y: int) -> int:
    return x + y


def subtract(x: int, y: int) -> int:
    return x - y


FN_MAP = {
    "add": add,
    "subtract": subtract,
}

if __name__ == "__main__":
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter another number: "))
    operation = input("Enter an operation: ")

    print(FN_MAP[operation](num_1, num_2))
