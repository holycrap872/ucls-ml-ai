TODO: Write a demo that shows why "shopping list" is wrong word since
we don't care about order and we would never have duplicates. Instead
would either be a "shopping set" (e.g., {"tuna", "ketchup"}) or
"shopping dictionary" (e.g., {"tuna": 4, "ketchup": 1}.

> Be sure to make this point over and over to your family, they'll love
it!

Something like:

```python
class GroceryStore:
    def __init__(self) -> None:
        self.aisle_1 = ["strawberry", "apple", "avocado"]
        self.aisle_2 = ["frozen_peas", "frozen_bananas", "ice_cream"]
        self.aisle_3 = ["dog_food", "light_bulbs", "mops"]

    def list_shop(self, list: typing.List[str]) -> None:
        """
        Wander all over the place
        """
        for item in list:
            found_item = False
            for aisle_item in self.aisle_1:
                if aisle_item == item:
                    print(f"Bought {item} from aisle 1")
                    found_item = True
                    break

            if found_item:
                 continue

            for aisle_item in self.aisle_2:
                if aisle_item == item:
                    print(f"Bought {item} from aisle 2")
                    found_item = True
                    break

            if found_item:
                 continue

            for aisle_item in self.aisle_3:
                if aisle_item == item:
                    print(f"Bought {item} from aisle 3")
                    found_item = True
                    break

            if found_item:
                 continue

            print(f"Going to have to order {item} online")

    def set_shop(self, set: typing.Set[str]) -> None:
        for aisle_item in aisle_1:
            for item in set:
                if aisle_item == item:
                    print(f"Bought {item} from aisle 1")

        ...


gc = GroceryStore()

shopping_list = ["strawberry", "mops", "apple"]
gc.list_shop(shopping_list)

shopping_set = {"strawberry", "mops", "apples"}
gc.set_shop(shopping_set)
```

EQs:
1. What is the only time where the shopping list is efficient (for the shopper)?
2. What would be the code for a shopping dictionary?
3. How could we simply the program with functions?
