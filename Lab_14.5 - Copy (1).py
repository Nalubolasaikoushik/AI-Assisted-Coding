import random
import re
import sys
import unicodedata


def normalize_text(text: str) -> str:
    normalized = unicodedata.normalize("NFC", text).casefold()
    return re.sub(r"[^\w\s]", "", normalized, flags=re.UNICODE).replace(" ", "")


def is_palindrome(text: str) -> bool:
    cleaned = normalize_text(text)
    return cleaned == cleaned[::-1]


def run_palindrome_tests() -> None:
    test_cases = [
        ("madam", True),
        ("racecar", True),
        ("hello", False),
        ("A man, a plan, a canal: Panama", True),
        ("No lemon, no melon", True),
        ("reifier", True),
        ("àbbà", True),
        ("😊abba😊", True),
        ("😊abc😊", False),
        ("", True),
        ("x", True),
        ("!!!", True),
        ("AñA", True),
    ]

    for text, expected in test_cases:
        result = is_palindrome(text)
        assert result == expected, f"Failed for {text!r}: expected {expected}, got {result}"

    print("Palindrome tests passed.")
    for text, _ in test_cases:
        print(f"is_palindrome({text!r}) -> {is_palindrome(text)}")


class SkipListNode:
    def __init__(self, value: int | None, level: int) -> None:
        self.value = value
        self.forward = [None] * (level + 1)


class SkipList:
    def __init__(self, max_level: int = 4, probability: float = 0.5) -> None:
        self.max_level = max_level
        self.probability = probability
        self.level = 0
        self.header = SkipListNode(None, max_level)

    def random_level(self) -> int:
        level = 0
        while random.random() < self.probability and level < self.max_level:
            level += 1
        return level

    def search(self, value: int) -> bool:
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        return current is not None and current.value == value

    def insert(self, value: int) -> None:
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]
        if current is not None and current.value == value:
            return

        new_level = self.random_level()
        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.header
            self.level = new_level

        new_node = SkipListNode(value, new_level)
        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def delete(self, value: int) -> None:
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]
        if current is None or current.value != value:
            return

        for i in range(self.level + 1):
            if update[i].forward[i] != current:
                continue
            update[i].forward[i] = current.forward[i]

        while self.level > 0 and self.header.forward[self.level] is None:
            self.level -= 1

    def to_list(self) -> list[int]:
        values = []
        current = self.header.forward[0]
        while current is not None:
            values.append(current.value)
            current = current.forward[0]
        return values


def run_skip_list_demo() -> None:
    random.seed(7)
    skip_list = SkipList(max_level=5)

    for value in [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]:
        skip_list.insert(value)

    print("\nSkip List contents after insertion:")
    print(skip_list.to_list())

    print("Search 19 ->", skip_list.search(19))
    print("Search 15 ->", skip_list.search(15))

    skip_list.delete(19)
    skip_list.delete(3)

    print("Skip List contents after deletion:")
    print(skip_list.to_list())
    print("Search 19 after deletion ->", skip_list.search(19))


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    print("Lab 14.5")
    print("-" * 20)
    run_palindrome_tests()
    run_skip_list_demo()


if __name__ == "__main__":
    main()
