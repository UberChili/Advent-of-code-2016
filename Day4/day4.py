#!/usr/bin/env python3

from sys import argv


def main():
    print("Hello")

    if len(argv) < 2:
        exit("Usage: python day4.py input")

    with open(argv[1], 'r') as fp:
        names = fp.strip().readlines()

    print(names)


if __name__ == "__main__":
    main()
