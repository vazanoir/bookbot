import sys
from os import path


def main():
    if len(sys.argv) < 2:
        print("error: no path to file given")
        sys.exit(1)

    for i in range(1, len(sys.argv)):
        arg = sys.argv[i]
        if path.isfile(arg):
            process_file(arg)


def process_file(file):
    with open(file) as f:
        file_contents = f.read()

        print(f"╺ {file} ╸")

        print("┌───────┬─────────────────┐")
        print(f"│ words │ {left_pad(str(word_count(file_contents)), 15)} │")
        print("└───────┴─────────────────┘")

        chars = char_count(file_contents)
        print("┌───────────┬─────────────┐")
        print("│ character │ occurrences │")
        print("├───────────┼─────────────┤")
        for c in sorted(chars, key=chars.get, reverse=True):
            if ord(c) in range(97, 123):
                print(f"│ {left_pad(c, 9)} │ {left_pad(str(chars[c]), 11)} │")
        print("└───────────┴─────────────┘\n\n")


def left_pad(str, size):
    for _ in range(size - len(str)):
        str = " " + str
    return str


def word_count(str):
    return len(str.split())


def char_count(str):
    count = {}

    for c in str.lower():
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    return count


main()
