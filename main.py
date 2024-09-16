def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(word_count(file_contents))
        print(char_count(file_contents))


def word_count(str):
    return len(str.split())


def char_count(str):
    count = {}

    for c in str.lower():
        if c in count:
            count[c] = count[c] + 1
        else:
            count[c] = 1

    return count


main()
