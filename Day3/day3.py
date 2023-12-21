#!/usr/bin/env python3

from sys import argv

def main():

    if len(argv) < 2:
        exit("usage: python day3.py input")

    filename = argv[1]

    with open(filename, 'r') as fp:
        triangles = fp.readlines()

    for triangle in triangles:
        print(triangle.strip())


if __name__ == "__main__":
    main()
