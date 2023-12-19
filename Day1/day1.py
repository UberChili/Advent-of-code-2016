#!/usr/bin/env python3

import re
import math
from sys import argv


class Position:
    def __init__(self, x, y):
        self.facing = 'N'
        self.x1 = 5
        self.y1 = 5
        self.x = 0
        self.y = 0

    def calc_trajectory(self):
        pass


def main():
    player = Position(0, 0)

    filename = argv[1]
    with open(filename, 'r') as fp:
        directions_str = fp.readline().replace(",", "").replace(" ", "")

    print(directions_str)
    dirs = re.findall(r'([LR]\d+)', directions_str)

    # print(dirs)
    for dir in dirs:
        side = dir[0]
        # steps = re.findall(r'([0-9]+)', dir)
        steps = re.search(r'([0-9]+)', dir)
        steps = int(steps.group(0))
        # move = (side, steps)
        # print(move)
        if player.facing == 'N':
            if side == 'R':
                player.facing = 'E'
                player.x += steps
            elif side == 'L':
                player.facing = 'W'
                player.x -= steps
        elif player.facing == 'S':
            if side == 'R':
                player.facing = 'W'
                player.x -= steps
            elif side == 'L':
                player.facing = 'E'
                player.x += steps
        elif player.facing == 'W':
            if side == 'R':
                player.facing = 'N'
                player.y += steps
            elif side == 'L':
                player.facing = 'S'
                player.y -= steps
        elif player.facing == 'E':
            if side == 'R':
                player.facing = 'S'
                player.y -= steps
            elif side == 'L':
                player.facing = 'N'
                player.y += steps

    print(player.facing, player.x, player.y)
    distance = abs(0 - player.x) + abs(0 - player.y)
    print(distance)


if __name__ == "__main__":
    main()
