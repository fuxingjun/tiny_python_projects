#!/usr/bin/env python3
"""
Author : jayden <jayden@localhost>
Date   : 2023-08-09
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('rt'),
                        default=open('gashlycrumb.txt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # line_dict = {}
    # for line in args.file:
    #     line_dict[line[0].upper()] = line.strip()

    line_dict = {line[0].upper(): line.rstrip() for line in args.file}

    while True:
        letter = input()
        print(line_dict.get(letter.upper(), f'I do not know "{letter}".'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
