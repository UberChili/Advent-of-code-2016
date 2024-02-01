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
    # pattern = r"((\d+)x(\d+))"
    # pattern = r"(\d+x\d+)"
    pattern = r"\(\d+x\d+\)"

    if m := re.finditer(pattern, s):
        # print(m.group(0).strip('()').split('x'))
        for match in m:
            # print(match.group(0))
            start_pos = match.start()
            end_pos = match.end()
            length, times = match.group(0).strip('()').split('x')
            chunk_to_delete = s[:start_pos] + s[end_pos:]
            # chunk_to_add = chunk_to_delete + s[end_pos + int(length) - 1]
            chunk_to_add = s[end_pos : end_pos + int(length)]
            print(chunk_to_add)
            # print(chunk)
            # s = s.replace(matech.group(0), '', 1)
        # current = m.group(0)
        # length, times = current.strip('()').split('x')
        # print(length, times)
        # s = s.replace(f"({length}x{times})", '', 1)
        # s = s.replace(current, '', 1)
    else:
        print("no pattern foudn")
        # print("pattern not found")


if __name__ == "__main__":
    main()
