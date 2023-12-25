#!/usr/bin/env python3

from sys import argv


def main():
    if len(argv) < 2:
        exit("Usage: python day6.py file")

    columns = {}
    with open(argv[1], 'r') as fp:
        lines = fp.readlines()

        for line in lines:
            print(line.strip())


if __name__ == "__main__":
    main()
