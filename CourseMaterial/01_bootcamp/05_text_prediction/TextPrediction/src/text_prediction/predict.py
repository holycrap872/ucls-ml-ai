import typing


class TextPredictor:
    def __init__(self) -> None:
        self._ngram_map = {}

    def ingest(self, file_path: str) -> None:
        with open(file_path, "r") as fd:
            prev_word = None

            for line in fd:
                for word in line.split(" "):
                    cur_word = word.strip().lower()
                    if cur_word not in self._ngram_map:
                        self._ngram_map[cur_word] = {}

                    if prev_word:
                        if prev_word not in self._ngram_map[cur_word]:
                            self._ngram_map[cur_word][prev_word] = 0

                        self._ngram_map[cur_word][prev_word] += 1

                    prev_word = cur_word

    def get_longest_word(self, hit_map: typing.Dict[str, int]) -> str:
        max_hit = None
        max_word = None
        for word, ite in hit_map.items():
            if not max_hit or ite > max_hit:
                max_hit = ite
                max_word = word
        return max_word

    def produce(self, start_word: str, length: int) -> None:
        start_word = start_word.lower()
        for _ in range(0, length):
            sub_map = self._ngram_map[start_word]
            next_word = self.get_longest_word(sub_map)

            print(start_word)
            start_word = next_word


if __name__ == "__main__":
        tp = TextPredictor()
        tp.ingest("bible.txt")
        tp.produce("thou", 10)
