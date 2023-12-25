#!/usr/bin/env python3

from collections import defaultdict
from sys import argv


def main():
    if len(argv) < 2:
        exit("Usage: python day6.py file")

    with open(argv[1], 'r') as fp:
        lines = fp.readlines()

    columns = defaultdict(list)
    for line in lines:
        for i in range(len(line.strip())):
            columns[i].append(line[i])

    message = ""
    for i in columns:
        # print(max(columns[i], key=columns[i].count))
        message += max(columns[i], key=columns[i].count)

    print(message)


if __name__ == "__main__":
    main()
