#!/usr/bin/env python3

import hashlib

def starts_with_zeros(hash: str) -> str:
    if hash[0] == '0' and hash[1] == '0' and hash[2] == '0' and hash[3] == '0' and hash[4] == '0':
        return True
    return False


def get_next(hash: str) -> str:
    return hash[5]


def main():
    example_input = "abc"
    puzz_input = "ugkcyxxp"
    password = ""

    # h = hashlib.new('md5')
    # h.update(b"abc3231929")
    # print(h.hexdigest())

    h = hashlib.new('md5')
    h.update(b"abc3231929")
    print(h.hexdigest())



if __name__ == "__main__":
    main()
