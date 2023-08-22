#!/usr/bin/env python3
"""
Author : jayden <jayden@localhost>
Date   : 2023-08-20
Purpose: Rock the Casbah
"""

import argparse
import os.path
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='File',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()
    if os.path.isfile(args.text):
        # outfile = f"{args.text}.out"
        # create_file(outfile, "")
        # args.outfile = open(outfile, "wt")
        args.text = open(args.text).read().rstrip()
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    reg = re.compile(r'(\W+)')

    for line in args.text.splitlines():
        # for word in re.split(r'(\W+)', line.rstrip()):
        #     print(fry(word), end='')
        # print("")
        # words = []
        # for word in re.split(r'(\W+)', line.rstrip()):
        #     words.append(fry(word))
        # print("".join(words), file=args.outfile if args.outfile else sys.stdout)

        # print("".join(map(fry, re.split(reg, line.rstrip()))), file=args.outfile if args.outfile else sys.stdout)
        print("".join(map(fry, reg.split(line.rstrip()))), file=args.outfile if args.outfile else sys.stdout)


def fry(word):
    # if word.lower() == 'you':
    #     return word[0] + "'all"
    match = re.match("([yY])ou", word)
    if match:
        return match.group(1) + "'all"

    # if word.endswith("ing"):
    #     return word[:-1] + "'"

    match = re.search("(.+)ing$", word)
    return match.group(1) + "in'" if match and re.search("[aeiouy]", match.group(1).lower()) else word


def create_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def test_fry():
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == "swing"


# --------------------------------------------------
if __name__ == '__main__':
    main()
