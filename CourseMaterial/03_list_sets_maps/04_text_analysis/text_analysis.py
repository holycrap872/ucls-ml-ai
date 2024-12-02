#!/usr/bin/env python3


def open_file(path: str) -> str:
    with open(path, "r") as fp:
        text = fp.read()
        return text


def normalize(text: str) -> list[str]:
    text = text.lower()
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("_", "")
    text = text.replace("'", "")
    text = text.replace('"', "")
    text = text.replace("?", "")
    text = text.replace("!", "")
    text = text.replace("-", " ")
    return text.split()


def create_count_dict(text: list[str]) -> dict[str, int]:
    count_dict: dict[str, int] = {}
    for word in text:
        if word not in count_dict:
            count_dict[word] = 0
        count_dict[word] += 1

    return count_dict


def max_find(count_dict: dict[str, int]) -> str | None:
    max_count = None
    word = None

    for k in count_dict:
        if max_count is None or count_dict[k] > max_count:
            max_count = count_dict[k]
            word = k

    return word


def jaccard_similarity(base_book_paths: list[str], compare_book_path: str) -> float:
    common_words = None
    for base_book_path in base_book_paths:
        words_in_book = set(open_file(base_book_path))
        if common_words is None:
            common_words = words_in_book
        else:
            common_words = common_words.intersection(words_in_book)

    compare_book_words = set(normalize(open_file(compare_book_path)))
    assert common_words is not None

    return len(common_words.intersection(compare_book_words)) / len(common_words.union(compare_book_words))


if __name__ == "__main__":
    rb_word_list = normalize(open_file("CourseMaterial/data/robert_frost.txt"))
    print(f"Words in Robert Frost: {len(rb_word_list)}")

    rb_word_set = set(rb_word_list)
    print(f"Unique words in Robert Frost: {len(rb_word_set)}")

    rb_count_dict = create_count_dict(rb_word_list)
    most_frequent_rb_word = max_find(rb_count_dict)
    print(f"Most frequent word in Robert Frost: {most_frequent_rb_word}")

    fr_word_list = set(normalize(open_file("CourseMaterial/data/frankenstein.txt")))
    print(f"Words in either RF and Frank: {len(rb_word_set.union(fr_word_list))}")
    print("Words in both RF and Frank:", len(rb_word_set.intersection(fr_word_list)))

    similarity_thriller = jaccard_similarity(
        [
            "CourseMaterial/data/dracula.txt",
            "CourseMaterial/data/the_time_machine.txt",
            "CourseMaterial/data/frankenstein.txt",
        ],
        "CourseMaterial/data/great_gatsby.txt",
    )
    print("Similarity to thriller:", similarity_thriller)

    similarity_drama = jaccard_similarity(
        [
            "CourseMaterial/data/pride_and_prejudice.txt",
            "CourseMaterial/data/oliver_twist.txt",
            "CourseMaterial/data/little_women.txt",
        ],
        "CourseMaterial/data/great_gatsby.txt",
    )
    print("Similarity to drama:", similarity_drama)
