#!/usr/bin/env python3
"""
Author : jayden <jayden@localhost>
Date   : 2023-08-20
Purpose: Rock the Casbah
"""

import argparse
import string
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme')

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='File',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


def stemmer(text):
    pattern = f"([{''.join([c for c in string.ascii_lowercase if c not in 'aeiou'])}]+)?([aeiou])(.*)"

    # match = re.match(pattern, args.word, re.IGNORECASE)
    text = text.lower()
    match = re.match(pattern, text)
    if match:
        p1 = match.group(1) or ''
        p2 = match.group(2) or ''
        p3 = match.group(3) or ''
        return p1, p2 + p3
    else:
        return text, ''


def stemmer2(text):
    text = text.lower()
    vowel_pos = list(map(text.index, filter(lambda v: v in text, 'aeiou')))

    if vowel_pos:
        first_vowel = min(vowel_pos)
        return text[:first_vowel], text[first_vowel:]
    else:
        return text, ''


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    t = stemmer(args.word)
    if not t[1]:
        print(f'Cannot rhyme "{args.word}"')
    else:
        prefix_list = [c for c in string.ascii_lowercase if c not in 'aeiou']
        prefix_list.extend(['bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr',
                            'pl', 'pr', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st',
                            'sw', 'th', 'tr', 'tw', 'thw', 'wh', 'wr', 'sch', 'scr', 'shr', 'sph',
                            'spl', 'spr', 'squ', 'str', 'thr'])
        consonant, vowel = t
        print('\n'.join(sorted([f'{c}{vowel}' for c in prefix_list if c != consonant])), file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()


def test_stemmer():
    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch', 'air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
    assert stemmer('123') == ('123', '')
