#!/usr/bin/env python3

"""
Java equivalent:

```
import java.util.HashMap;
import java.util.Map;

interface Pluggable {
    String plugin();
}

class Refrigerator implements Pluggable {
    @Override
    public String plugin() {
        return "Making stuff cold";
    }
}

class Microwave implements Pluggable {
    @Override
    public String plugin() {
        return "Making stuff hot";
    }
}

class Wall {
    public static void main(String[] args) {
        Map<String, Pluggable> applianceMap = new HashMap<>();
        applianceMap.put("fridge", new Refrigerator());
        applianceMap.put("micro", new Microwave());

        String applianceChoice = "fridge";

        Pluggable appliance = applianceMap.get(applianceChoice);
        if (appliance != null) {
            System.out.println("Result: " + appliance.plugin());
        } else {
            System.out.println("Invalid operation");
        }
    }
}
```
"""


def refrigerator() -> str:
    return "Making stuff cold"


def microwave() -> str:
    return "Making stuff hot"


FN_MAP = {
    "fridge": refrigerator,
    "micro": microwave,
}

if __name__ == "__main__":
    appliance = input("Enter an appliance: ")

    print(FN_MAP[appliance]())
