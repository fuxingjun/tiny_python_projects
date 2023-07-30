#!/usr/bin/env python3
"""
Author : jayden <jayden@localhost>
Date   : 2023-07-30
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='word', help='A word')
    parser.add_argument('-s', '--starboard', help='side flag', action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    word = args.word
    side = 'starboard' if args.starboard else 'larboard'
    char = word[0].lower()
    article = 'an' if char in 'aeiou' else 'a'
    print(f"Ahoy, Captain, {article} {word} off the {side} bow!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
