#!/usr/bin/env python3


from collections import deque
import re
import numpy as np
import sys


def main():
    height = 3
    width = 7

    # screen = [['.' for i in range(width)] for j in range(height)]
    # [print(row) for row in screen]
    # print(screen)
    # draw_screen(screen)

    screen = np.chararray((6, 50), unicode=True)
    screen[:] = '.'
    # draw_screen(screen)

    if len(sys.argv) < 2:
        sys.exit("Bad cmdline arguments")

    with open(sys.argv[1]) as fp:
        lines = [line.strip().split(' ') for line in fp.readlines()]

    # print("/")
    for line in lines:
        if line[0] == "rect":
            add_rect(line[1], screen)
        elif line[0] == "rotate":
            instructions = parse_line(line)
            rotate(instructions, screen)
    draw_screen(screen)
    print(calc_leds(screen))


def calc_leds(screen):
    return np.count_nonzero(screen == '#')

def rotate(inst, screen):
    if 'dir' not in inst:
        sys.exit("Error, not a dict passed to rotate")

    # print(inst)
    if inst['dir'] == 'x':
        # screen[:, 0] = screen[:, 0]
        # screen[:, inst['n']]
        qu = deque(screen[:, inst['n']])
        qu.rotate(inst['times'])
        screen[:, inst['n']] = list(qu)
    elif inst['dir'] == 'y':
        qu = deque(screen[inst['n'], :])
        qu.rotate(inst['times'])
        screen[inst['n'], :] = list(qu)


def parse_line(line):
    direction, n = line[2].split('=')
    times = int(line[-1])
    return {"dir": direction, "n": int(n), "times": times}


def add_rect(inst, screen):
    cols, rows = inst.split('x')
    for row in range(int(rows)):
        for col in range(int(cols)):
            screen[row, col] = '#'


def draw_screen(screen):
    for row in screen:
        for c in row:
            print(c, end="")
        print()


if __name__ == "__main__":
    main()
