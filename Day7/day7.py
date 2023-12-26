#!/usr/bin/env python3

from sys import argv
import re


def get_rest(line:str) -> str:
    hyper = re.findall(r'(\[[a-z]+\])', line)[0]
    new_line = line.replace(hyper, "|")
    return (new_line.split("|"))

def get_hypernet(line: str) -> str:
    return re.findall(r'(\[[a-z]+\])', line)[0].strip("[]")

def has_abba(line:str) -> bool:
    for i in range(2, len(line), 2):
        first = line[i - 2]
        second = line[i - 1]
        # if line[i] == second and line[i + 1] == first:
        if line[i] == second and line[i + 1] == first and first != second and line[i] != line[i + 1]:
            return True
    return False

def main():
    if len(argv) != 2:
        exit("Usage: python day7.py input_file")

    with open(argv[1], 'r') as fp:
        lines = [x.strip() for x in fp.readlines()]

    counter = 0
    for line in lines:
        hypernet = get_hypernet(line)
        if has_abba(hypernet):
            continue
        else:
            for substring in get_rest(line):
                if has_abba(substring):
                    counter += 1
                    continue

    print(counter)

if __name__ == "__main__":
    main()
