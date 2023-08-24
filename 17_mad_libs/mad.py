#!/usr/bin/env python3
"""
Author : jayden <jayden@localhost>
Date   : 2023-08-25
Purpose: Rock the Casbah
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='File',
                        help='Input file',
                        type=argparse.FileType('rt'))

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        metavar='input',
                        nargs="*",
                        type=str,
                        default=None)

    args = parser.parse_args()
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    text = args.file.read().rstrip()
    matches = re.findall("(<([^<>]+)>)", text)
    # if not re.search("(<(.+?)>)", text):
    if not matches:
        # print(f'"{args.file.name}" has no placeholders.', file=sys.stderr)
        # sys.exit(1)
        sys.exit(f'"{args.file.name}" has no placeholders.')
    for placeholder, name in matches:
        value = args.inputs.pop(0) if args.inputs else input(
            f'Give me {"an" if name[0].lower() in "aeiou" else "a"} {name}: ')
        text = re.sub(placeholder, value, text, count=1)

    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
