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

    int i_1 = 5;
    int i_2 = 4;
    String operation = "add";

    Operation op = operationMap.get(operation);
    if (op != null) {
      System.out.println("Result: " + op.operate(i_1, i_2));
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
    i_1 = int(input("Enter an int: "))
    i_2 = int(input("Enter an int: "))
    operation = input("Enter an op: ")

    print(FN_MAP[operation](i_1, i_1))
