#!/usr/bin/env python3

import re
import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Incorrect cmdline arguments")


    with open(sys.argv[1]) as fp:
        lines = [line.strip() for line in fp.readlines()]

    for line in lines:
        catch(line)


def catch(s):
    pattern = r"((\d)x(\d))"

    if m := re.search(pattern, s):
        length, times = [int(x) for x in m.group(1).split('x')]
        # print(m.group(0))
        n_s = s.replace(f"({length}x{times})", '', 1)
        print(n_s)
    else:
        print("pattern not found")



if __name__ == "__main__":
    main()
