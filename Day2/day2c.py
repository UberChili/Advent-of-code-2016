#!/usr/bin/env python3

from sys import argv


def main():
    if len(argv) != 2:
        print("Usage: python day2c.py input")
        exit()

    numpad = [
        ['0', '0', '1', '0', '0'],
        ['0', '2', '3', '4', '0'],
        ['5', '6', '7', '8', '9'],
        ['0', 'A', 'B', 'C', '0'],
        ['0', '0', 'D', '0', '0']
    ]

    with open(argv[1], 'r') as fp:
        code = ""
        row = 2
        col = 0

        for steps_line in fp.readlines():
            steps_line.strip()
            for step in steps_line:
                if step == 'U':
                    if (0 <= row - 1 < len(numpad)) and (numpad[row - 1][col] != '0'):
                        row -= 1
                if step == 'D':
                    if (0 <= row + 1 < len(numpad)) and (numpad[row + 1][col] != '0'):
                        row += 1
                if step == 'L':
                    if (0 <= col - 1 < len(numpad[row])) and (numpad[row][col - 1] != '0'):
                        col -= 1
                if step == 'R':
                    if (0 <= col + 1 < len(numpad[row])) and (numpad[row][col + 1] != '0'):
                        col += 1
            code += numpad[row][col]
    print(code)


if __name__ == "__main__":
    main()
