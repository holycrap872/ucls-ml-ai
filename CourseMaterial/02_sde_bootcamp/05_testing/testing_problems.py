# Bug: Fails with empty list
def average(numbers: list[int]) -> float:
    # Assumes the list is non-empty.
    return sum(numbers) / len(numbers)


assert average([5, 6, 7]) == 6.0
assert average([2, 2, 2]) == 2.0
try:
    assert average([])
except ZeroDivisionError:
    pass
else:
    assert False


# Bug: Assumes that words can't be over 100 chars in length
def contains_an_a(word: str) -> bool:
    for i in range(100):
        if i < len(word) and word[i] == "a":
            return True

    return False


assert contains_an_a("hello") == False
assert contains_an_a("halo") == True
try:
    assert contains_an_a("b" * 1000 + "a") == True
except AssertionError:
    pass
else:
    assert False


# Bug: misses a case
def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    if a == b or b == c:
        return "Isosceles"
    else:
        return "Scalene"


assert triangle_type(3, 3, 3) == "Equilateral"
assert triangle_type(3, 3, 4) == "Isosceles"
assert triangle_type(3, 4, 5) == "Scalene"
try:
    assert triangle_type(3, 4, 3) == "Isosceles"
except AssertionError:
    pass
else:
    assert False


# Bug: bug occurs b/c doesn't handle <=
def find_middle(a: int, b: int, c: int) -> int:
    if a < b < c:
        return b
    elif a < c < b:
        return c
    elif b < c < a:
        return c
    elif b < a < c:
        return a
    elif c < a < b:
        return a
    else:
        return b


assert find_middle(8, 4, 10) == 8
assert find_middle(4, 8, 10) == 8
assert find_middle(10, 4, 8) == 8
try:
    assert find_middle(10, 4, 10) == 10
except AssertionError:
    pass
else:
    assert False


def categorize_grade(grade):
    # Categorizes numerical grades into letter grades but has a logical error due to the use of else.
    letter_grade = ""
    if grade >= 97:
        letter_grade = "A+"
    if grade >= 93:
        letter_grade = "A"
    elif grade >= 90:
        letter_grade = "A-"
    elif grade >= 87:
        letter_grade = "B+"
    elif grade >= 83:
        letter_grade = "B"
    elif grade >= 80:
        letter_grade = "B-"
    elif grade >= 77:
        letter_grade = "C+"
    elif grade >= 73:
        letter_grade = "C"
    elif grade >= 70:
        letter_grade = "C-"
    elif grade >= 67:
        letter_grade = "D+"
    elif grade >= 63:
        letter_grade = "D"
    elif grade >= 60:
        letter_grade = "D-"
    else:
        letter_grade = "F"

    return letter_grade


assert categorize_grade(60) == "D-"
assert categorize_grade(95) == "A"
try:
    assert categorize_grade(97) == "A+"
except AssertionError:
    pass
else:
    assert False


# Bug: Returns true if the the first letters are the same
def palindrome_checker(word: str) -> bool:
    for i in range(len(word) // 2):
        if word[i] == word[-1 + -i]:
            return True

    return False


assert palindrome_checker("hello") == False
assert palindrome_checker("racecar") == True
try:
    assert palindrome_checker("yummy") == False
except AssertionError:
    pass
else:
    assert False


# Bug: Off by one error
def count_matches(l: list[str], word: str):
    matches = 0
    for i in range(len(l) - 1):
        if l[i] == word:
            matches += 1
    return matches


assert count_matches(["hey", "you"], "guys") == 0
assert count_matches(["hey", "you"], "hey") == 1
try:
    assert count_matches(["hey", "hey", "hey"], "hey") == 3
except AssertionError:
    pass
else:
    assert False


# Bug: Fails when s is either empty
def capitalize_first(s: str) -> str:
    return s[0].upper() + s[1:]


assert capitalize_first("Eric") == "Eric"
assert capitalize_first("eric") == "Eric"
try:
    assert capitalize_first("")
except IndexError:
    pass
else:
    assert False


# Bug: Function returns False too early
def find_in_list(lst: list[int], item: int) -> bool:
    for i in lst:
        if i == item:
            return True
        elif i > item:
            return False
    return False


assert find_in_list([1, 3, 5, 7], 3) == True
assert find_in_list([1, 3, 5, 7], 4) == False
try:
    assert find_in_list([7, 5, 3, 1], 3) == True
except AssertionError:
    pass
else:
    assert False


# Bug: Assumes the strings are of equal length
def strings_equal(s1: str, s2: str) -> bool:
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


assert strings_equal("hello", "hello") == True
assert strings_equal("shops", "ships") == False
try:
    assert strings_equal("hellothere", "hello") == False
except IndexError:
    pass
else:
    assert False


# Bug: The function assumes the list is always non-empty
def max_number(numbers: list[int]) -> int:
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num


assert max_number([1, 3, 5, 7]) == 7
assert max_number([3, 5, 7, 1]) == 7
try:
    assert max_number([]) == True
except IndexError:
    pass
else:
    assert False


def run_command(command: str, *, is_admin: bool) -> str:
    admin_only = ["remove", "download", "create"]
    if not is_admin:
        for c in admin_only:
            if c == command or c.upper() == command:
                return "Sorry, that's only for admin"

    return f"Executed command {command.lower()}"


assert run_command("remove", is_admin=True) == "Executed command remove"
assert run_command("remove", is_admin=False) == "Sorry, that's only for admin"
try:
    assert run_command("rEmovE", is_admin=False) == "Sorry, that's only for admin"
except AssertionError:
    pass
else:
    assert False


# Bug: Fails to check for the position of . which should be after @
def is_valid_email(email: str) -> bool:
    # Checks if an email is valid based on simplistic criteria.
    return "@" in email and "." in email.split("@")[1]


assert is_valid_email("tmp@e.com") == True
assert is_valid_email("tmp.com") == False
try:
    assert is_valid_email("tmp.e@com") == True
except AssertionError:
    pass
else:
    assert False


# Bug: The function fails for negative numbers due to the negative sign.
def sum_of_digits(n: int) -> int:
    # Returns the sum of the digits in the integer n.
    return sum(int(char) for char in str(n))


assert sum_of_digits(1) == 1
assert sum_of_digits(123) == 6
try:
    assert sum_of_digits(-123) == 5
except ValueError:
    pass
else:
    assert False


# Bug: Fails to handle cases where currency is not in rates dictionary
def convert_to_usd(amount: int, currency: str) -> float:
    # Converts an amount from a specified currency to USD.
    rates = {"EUR": 1.1, "JPY": 0.0091}
    return amount * rates[currency]


assert convert_to_usd(10, "EUR") == 11.0
assert convert_to_usd(100, "JPY") == 0.91
try:
    assert convert_to_usd(10, "HSD") == 10
except KeyError:
    pass
else:
    assert False


def authenticate(password: str) -> bool:
    # Mimics a buffer overflow vulnerability - a classic error in languages like C
    buffer = [""] * 10
    for i in range(len(password)):
        buffer[i] = password[i]
    return buffer == ["s", "e", "c", "r", "e", "t", "", "", "", ""]


assert authenticate("guess") == False
assert authenticate("secret") == True
try:
    assert authenticate("long password")
except IndexError:
    pass
else:
    assert False


# Bug: Off-by-one error that manifests only if the list length is odd
def pair_items_in_list(items: list[int]) -> list[tuple[int, int]]:
    processed = []

    i = 0
    while i < len(items) - 1:
        # Processes in pairs
        processed.append((items[i], items[i + 1]))
        i += 2

    return processed


assert pair_items_in_list([1, 2, 5, 9, 0, 0]) == [(1, 2), (5, 9), (0, 0)]
try:
    assert pair_items_in_list([1, 2, 3]) == [(1, 2), (3, None)]
except AssertionError:
    pass
else:
    assert False


# Bug: Incorrect for even-length lists
def find_median(numbers: list[int]) -> int:
    sorted_numbers = sorted(numbers)
    return sorted_numbers[len(sorted_numbers) // 2]


assert find_median([1, 2, 4]) == 2
assert find_median([1, 2, 2, 5]) == 2
try:
    assert find_median([1, 2, 4, 5]) == 3
except AssertionError:
    pass
else:
    assert False
