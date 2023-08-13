#!/usr/bin/env python3
"""
Author : jayden <jayden@localhost>
Date   : 2023-08-13
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f"--number {args.num} must be greater than 0")
    return parser.parse_args()


def verse(bottle):
    """String a verse"""
    s1 = "" if bottle == 1 else "s"
    s2 = "" if bottle == 2 else "s"
    return '\n'.join([
        f'{bottle} bottle{s1} of beer on the wall,',
        f'{bottle} bottle{s1} of beer,',
        'Take one down, pass it around,',
        f'{"No more" if bottle == 1 else bottle - 1} bottle{s2} of beer on the wall!'
    ])


def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    last_verse = verse(2)
    assert last_verse == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,',
        '1 bottle of beer on the wall!'
    ])


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # reversed(range(args.num))
    # solution 1
    # for i in range(args.num, 0, -1):
    #     print(verse(i) + ('' if i == 1 else "\n"))

    # for i in range(args.num, 0, -1):
    #     print(verse(i), end='\n' if i == 1 else "\n\n")

    # solution 2
    print("\n\n".join(map(verse, range(args.num, 0, -1))))


# --------------------------------------------------
if __name__ == '__main__':
    main()
