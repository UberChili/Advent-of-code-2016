#!/usr/bin/env python3

from sys import argv


def main():
    if len(argv) != 2:
        print("Usage: python day2.py input")
        exit()

    numpad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    with open(argv[1], 'r') as fp:
        code = ""
        cursor = [1, 1]
        for steps_line in fp.readlines():
            steps_line.strip()
            for step in steps_line:
                if step == 'U':
                    if 0 <= (cursor[0] - 1) < len(numpad):
                        cursor[0] -= 1
                elif step == 'D':
                    if 0 <= (cursor[0] + 1) < len(numpad):
                        cursor[0] += 1
                elif step == 'L':
                    if 0 <= (cursor[1] - 1) < len(numpad):
                        cursor[1] -= 1
                elif step == 'R':
                    if 0 <= (cursor[1] + 1) < len(numpad):
                        cursor[1] += 1

            code += numpad[cursor[0]][cursor[1]]

    print(code)


if __name__ == "__main__":
    main()
