#!/usr/bin/env python3
"""
Author : jayden <jayden@localhost>
Date   : 2023-08-24
Purpose: Rock the Casbah
"""

import argparse
import os.path
import random
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble the letters of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help="Random seed",
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def scramble(word):
    if len(word) <= 3:
        return word
    mid_list = list(word[1:-1])
    random.shuffle(mid_list)

    return word[0] + ''.join(mid_list) + word[-1]


def test_scramble():
    state = random.getstate()
    random.seed(1)
    assert scramble("a") == "a"
    assert scramble("ab") == "ab"
    assert scramble("abc") == "abc"
    assert scramble("abcd") == "acbd"
    assert scramble("abcde") == "acbde"
    assert scramble("abcdef") == "aecbdf"
    assert scramble("abcde'f") == "abcd'ef"
    random.setstate(state)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    reg = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")
    
    random.seed(args.seed)
    for line in args.text.splitlines():
        print("".join([scramble(word) for word in re.split(reg, line)]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
