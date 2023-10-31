#!/usr/bin/env python3
import typing


def load_book(path: str) -> typing.List[str]:
    with open(path, "r") as fp:
        text = fp.read()
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


def get_num_words(text: typing.List[str]) -> int:
    return len(text)


def create_count_dict(text: typing.List[str]) -> typing.Dict[str, int]:
    count_dict = {}
    for word in text:
        if word not in count_dict:
            count_dict[word] = 0
        count_dict[word] += 1

    return count_dict


def max_find(count_dict: typing.Dict[str, int]) -> str:
    max_count = 0
    word = ""

    for k in count_dict:
        if count_dict[k] > max_count:
            max_count = count_dict[k]
            word = k

        if count_dict[k] == 1:
            print(k)

    return word


def jaccard_similarity(base_book_paths: typing.List[str], compare_book_path: str) -> float:
    common_words = None
    for base_book_path in base_book_paths:
        words_in_book = set(load_book(base_book_path))
        if common_words is None:
            common_words = words_in_book
        else:
            common_words = common_words.intersection(words_in_book)

    compare_book_words = set(load_book(compare_book_path))
    assert common_words is not None

    return len(common_words.intersection(compare_book_words)) / len(common_words.union(compare_book_words))


if __name__ == "__main__":
    rb_word_list = load_book("CourseMaterial/data/robert_frost.txt")
    fr_word_list = load_book("CourseMaterial/data/frankenstein.txt")

    print("Words in Robert Frost:", get_num_words(rb_word_list))
    print("Words in Frankenstein:", get_num_words(rb_word_list))

    rb_count_dict = create_count_dict(rb_word_list)
    fr_count_dict = create_count_dict(fr_word_list)

    rb_word_set = set(rb_word_list)
    fr_word_set = set(fr_word_list)

    print("Unique words in Robert Frost:", len(rb_word_set))
    print("Unique words in Frankenstein:", len(fr_word_set))

    print("Words in either RF and Frank:", len(rb_word_set.union(fr_word_list)))
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
