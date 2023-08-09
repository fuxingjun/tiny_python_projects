#!/usr/bin/env python3
"""
Author : jayden <jayden@localhost>
Date   : 2023-08-09
Purpose: Rock the Casbah
"""

import argparse
import os.path
from io import StringIO
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='str',
                        type=str,
                        # choices=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'],
                        choices=list('aeiou'),
                        default='a')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    lookup = {}
    for char in 'aeiouAEIOU':
        lookup[char] = args.vowel if char in 'aeiou' else args.vowel.upper()

    """
    solution-1
    """
    # fh = open(args.text) if os.path.isfile(args.text) else StringIO(args.text)
    # new_text = ''
    # for line in fh:
    #     for char in line:
    #         new_text += lookup.get(char, char)
    # print(new_text)

    """
    solution-2
    """
    # text = open(args.text).read() if os.path.isfile(args.text) else args.text
    # new_text = text.translate(str.maketrans(lookup))
    # print(new_text)

    """
    solution-2-1
    """
    # text = open(args.text).read() if os.path.isfile(args.text) else args.text
    # new_text = text.translate(str.maketrans('aeiouAEIOU', args.vowel * 5 + args.vowel.upper() * 5))
    # print(new_text)

    """
    solution-3
    """
    # new_text = open(args.text).read() if os.path.isfile(args.text) else args.text
    # for char in list('aeiouAEIOU'):
    #     new_text = new_text.replace(char, lookup[char])
    # print(new_text)

    """
    solution-4
    """
    # new_text = open(args.text).read() if os.path.isfile(args.text) else args.text
    # for char in list('aeiou'):
    #     new_text = new_text.replace(char, args.vowel).replace(char.upper(), args.vowel.upper())
    # print(new_text)

    """
    solution-5
    """
    # text = open(args.text).read() if os.path.isfile(args.text) else args.text
    # vowel = args.vowel
    # new_text = [vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c for c in text]
    # print(''.join(new_text))

    """
    solution-6
    """
    # text = open(args.text).read() if os.path.isfile(args.text) else args.text
    # vowel = args.vowel
    # new_text = map(lambda c: vowel if c in 'aeiou' else vowel.upper() if c in 'AEIOU' else c, text)
    # print(''.join(new_text))

    """
    solution-7
    """
    text = open(args.text).read() if os.path.isfile(args.text) else args.text
    text = re.sub('[AEIOU]', args.vowel.upper(), re.sub('[aeiou]', args.vowel, text))
    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
