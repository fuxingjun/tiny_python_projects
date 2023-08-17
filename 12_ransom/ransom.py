#!/usr/bin/env python3
"""
Author : jayden <jayden@localhost>
Date   : 2023-08-17
Purpose: Rock the Casbah
"""

import argparse
import os.path
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Ransom seed',
                        metavar='str',
                        type=int,
                        default=None)

    args = parser.parse_args()
    args.text = open(args.text).read().rstrip() if os.path.isfile(args.text) else args.text
    return args


def choose(char):
    return random.choice([char.lower(), char.upper()])


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    # print(''.join(map(choose, list(args.text))))

    print(''.join([choose(item) for item in list(args.text)]))


# --------------------------------------------------
if __name__ == '__main__':
    main()


def test_choose():
    state = random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'C'
    assert choose('d') == 'd'
    random.setstate(state)
