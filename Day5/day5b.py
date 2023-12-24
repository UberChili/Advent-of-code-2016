#!/usr/bin/env python3

import hashlib

def starts_with_zeros(hash: str) -> str:
    if hash[0] == '0' and hash[1] == '0' and hash[2] == '0' and hash[3] == '0' and hash[4] == '0':
        return True
    return False


def get_pos(hash: str) -> str:
    return hash[5]

def get_char(hash: str) -> str:
    return hash[6]


def main():
    example_input = "abc"
    puzz_input = "ugkcyxxp"
    password = [None] * 8

    integer = 0
    times = 0
    while True:
        test = puzz_input + str(integer)
        hash = hashlib.md5(test.encode()).hexdigest()
        integer += 1

        if starts_with_zeros(hash):
            pos = get_pos(hash)
            if pos.isdigit() and int(pos) < 8:
                if password[int(pos)] == None:
                    password[int(pos)] = get_char(hash)
                    times += 1
            else:
                continue
        elif times == 8:
            break

    for i in password:
        print(i, end="")
    print()


if __name__ == "__main__":
    main()
