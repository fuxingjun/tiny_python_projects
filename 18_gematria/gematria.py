#!/usr/bin/env python3
"""
Author : jayden <jayden@localhost>
Date   : 2023-08-26
Purpose: Rock the Casbah
"""

import argparse
import os.path
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for line in args.text.splitlines():
        print(" ".join([word2num(word) for word in line.split()]))

    # --------------------------------------------------


def word2num(word):
    return str(sum(map(ord, re.sub(r"[^A-Za-z0-9\s]", "", word))))


def test_word2num():
    assert word2num("a") == "97"
    assert word2num("abc") == "294"
    assert word2num("ab'c") == "294"
    assert word2num("4a-b'c,") == "346"


if __name__ == '__main__':
    main()
