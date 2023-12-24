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

    # print(hashlib.md5(example_input.encode()).hexdigest())

    integer = 0
    while True:
        test = puzz_input + str(integer)
        hash = hashlib.md5(test.encode()).hexdigest()
        integer += 1

        if starts_with_zeros(hash):
            password += get_next(hash)
        elif len(password) == 8:
            break

    print(password)


if __name__ == "__main__":
    main()
