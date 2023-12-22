#!/usr/bin/env python3
import re
from sys import argv


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_possible(self):
        if ((self.a + self.b) > self.c) and ((self.a + self.c) > self.b) and ((self.b + self.c) > self.a):
            return True
        return False


def main():
    if len(argv) < 2:
        exit("usage: python day3.py input")
    filename = argv[1]

    with open(filename, 'r') as fp:
        triangles_string = fp.readlines()

    triangles = []
    for triangle in triangles_string:
        triangles.append(re.findall(r'([0-9]+)', triangle))

    triangles = [[int(num) for num in triangle] for triangle in triangles]

    counter = 0
    for triangle in triangles:
        curr_triangle = Triangle(triangle[0], triangle[1], triangle[2])
        if curr_triangle.is_possible():
            counter += 1
    print(counter)


if __name__ == "__main__":
    main()
