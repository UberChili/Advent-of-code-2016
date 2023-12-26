#!/usr/bin/env python3

from sys import argv
import re


def get_hypernet(line: str) -> str:
    return re.findall(r'(\[[a-z]+\])', line)



def main():
    if len(argv) != 2:
        exit("Usage: python day7.py input_file")

    with open(argv[1], 'r') as fp:
        lines = [x.strip() for x in fp.readlines()]

    for line in lines:
        print(get_hypernet(line))


if __name__ == "__main__":
    main()
