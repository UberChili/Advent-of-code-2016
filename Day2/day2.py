#!/usr/bin/env python3

from sys import argv


class Numpad:
    def __init__(self):
        self.last = ''
        self.edges = [1, 2, 3, 4, 6, 7, 8, 9]

    def valid_move(self):
        if self.last in


def main():
    if len(argv) != 2:
        print("Usage: python day2.py input")
        exit()

    with open(argv[1], 'r') as fp:
        lines = fp.readlines()

        for line in lines:
            print(line.strip())


if __name__ == "__main__":
    main()
