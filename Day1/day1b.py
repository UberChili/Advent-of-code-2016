#!/usr/bin/env python3

import re
import math
from sys import argv


class Position:
    def __init__(self, x, y):
        self.facing = 'N'
        self.x = 0
        self.y = 0
        self.visited = []

    def have_visited(self):
        if (self.x, self.y) in self.visited:
            return True
        return False


def main():
    player = Position(0, 0)

    filename = argv[1]
    with open(filename, 'r') as fp:
        directions_str = fp.readline().replace(",", "").replace(" ", "")

    print(directions_str)
    dirs = re.findall(r'([LR]\d+)', directions_str)

    for dir in dirs:
        side = dir[0]
        steps = re.search(r'([0-9]+)', dir)
        steps = int(steps.group(0))
        if player.facing == 'N':
            if side == 'R':
                player.facing = 'E'
                for i in range(steps):
                    player.x += 1
                    if player.have_visited():
                        distance = abs(0 - player.x) + abs(0 - player.y)
                        print(distance)
                        exit()
                    else:
                        player.visited.append((player.x, player.y))
            elif side == 'L':
                player.facing = 'W'
                for i in range(steps, 0, -1):
                    player.x -= 1
                    if player.have_visited():
                        distance = abs(0 - player.x) + abs(0 - player.y)
                        print(distance)
                        exit()
                    else:
                        player.visited.append((player.x, player.y))
        elif player.facing == 'S':
            if side == 'R':
                player.facing = 'W'
                for i in range(steps, 0, -1):
                    player.x -= 1
                    if player.have_visited():
                        distance = abs(0 - player.x) + abs(0 - player.y)
                        print(distance)
                        exit()
                    else:
                        player.visited.append((player.x, player.y))
            elif side == 'L':
                player.facing = 'E'
                for i in range(steps):
                    player.x += 1
                    if player.have_visited():
                        distance = abs(0 - player.x) + abs(0 - player.y)
                        print(distance)
                        exit()
                    else:
                        player.visited.append((player.x, player.y))
        elif player.facing == 'W':
            if side == 'R':
                player.facing = 'N'
                for i in range(steps):
                    player.y += 1
                    if player.have_visited():
                        distance = abs(0 - player.x) + abs(0 - player.y)
                        print(distance)
                        exit()
                    else:
                        player.visited.append((player.x, player.y))
            elif side == 'L':
                player.facing = 'S'
                for i in range(steps, 0, -1):
                    player.y -= 1
                    if player.have_visited():
                        distance = abs(0 - player.x) + abs(0 - player.y)
                        print(distance)
                        exit()
                    else:
                        player.visited.append((player.x, player.y))
        elif player.facing == 'E':
            if side == 'R':
                player.facing = 'S'
                for i in range(steps, 0, -1):
                    player.y -= 1
                    if player.have_visited():
                        distance = abs(0 - player.x) + abs(0 - player.y)
                        print(distance)
                        exit()
                    else:
                        player.visited.append((player.x, player.y))
            elif side == 'L':
                player.facing = 'N'
                for i in range(steps):
                    player.y += 1
                    if player.have_visited():
                        distance = abs(0 - player.x) + abs(0 - player.y)
                        print(distance)
                        exit()
                    else:
                        player.visited.append((player.x, player.y))


if __name__ == "__main__":
    main()
