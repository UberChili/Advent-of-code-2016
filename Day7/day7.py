#!/usr/bin/env python3

import re
import sys


def main():

    if len(sys.argv) < 2:
        sys.exit("Bad cmdline arguments")

    with open(sys.argv[1]) as fp:
        lines = [line.strip() for line in fp.readlines()]

    for line in lines:
        if m := re.search('\[[a-zA-Z]+\]', line):
            hypernet = m.group(0)
            first, second = line.split(hypernet)
            # print(first, hypernet, second)
            has_abba(first)


def has_abba(s):
    # chunks = re.findall('.{2}', s)
    # print(chunks)
    for i in range(2, len(s), 2):
        last_chunk = s[i-2:i]
        rev_curr = s[i:i+2][::-1]
        print(last_chunk, rev_curr)


if __name__ == "__main__":
    main()
