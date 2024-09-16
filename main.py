def main():
    file = "books/frankenstein.txt"
    with open(file) as f:
        file_contents = f.read()
        print(f"--- Begin report of {file} ---")
        print(f"{word_count(file_contents)} words found in the document\n")
        chars = char_count(file_contents)
        for c in sorted(chars, key=chars.get, reverse=True):
            print(f"The '{c}' character was found {chars[c]} times")
        print("--- End report ---")


def word_count(str):
    return len(str.split())


def char_count(str):
    count = {}

    for c in str.lower():
        if ord(c) in range(97, 123):
            if c in count:
                count[c] = count[c] + 1
            else:
                count[c] = 1

    return count


main()
