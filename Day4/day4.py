#!/usr/bin/env python3

import re
from sys import argv


def get_checksum(line: str) -> str:
    return re.findall(r'(\[[a-z]+\])', line)[0].strip("[]")


def get_id(line: str) -> int:
    return int(re.findall(r'([0-9]+)', line)[0])


def get_letters(line: str) -> list:
    letters = []
    for i in line:
        if i.isalpha():
            letters.append(i)
        elif i.isdigit():
            break
    return letters


def get_counts(letters: list, checksum: str) -> map:
    counts = {}
    for i in checksum:
        counts[i] = letters.count(i)
    return counts


def get_occurrences(letters: list) -> map:
    counts = {}
    for letter in letters:
        counts[letter] = letters.count(letter)
    return counts

def main():
    if len(argv) < 2:
        exit("Usage: python day4.py input")

    with open(argv[1], 'r') as fp:
        names = [name.strip() for name in fp.readlines()]

    # for name in names:
    #     print(get_letters(name), get_id(name), get_checksum(name))

    letter_occurrences = {}
    for name in names:
        # print(get_letters(name))
        # print(get_letters(name), get_id(name), get_checksum(name))
        letter_occurrences = get_occurrences(get_letters(name))
        for i in letter_occurrences:
            print(f"{i}: {letter_occurrences[i]}, ", end="")
        print("\n")
        # counts = get_counts(get_letters(name), get_checksum(name))
        # for i in counts:
        #     print(f"{i}: {counts[i]} ", end="")
        # print("\n")


if __name__ == "__main__":
    main()
