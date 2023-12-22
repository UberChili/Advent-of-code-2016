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
        if i != '-' and i.isalpha:
            letters.append(i)
    return letters


def main():
    if len(argv) < 2:
        exit("Usage: python day4.py input")

    with open(argv[1], 'r') as fp:
        names = [name.strip() for name in fp.readlines()]

    for name in names:
        print(get_letters(name), get_id(name), get_checksum(name))

if __name__ == "__main__":
    main()
