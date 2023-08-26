#!/usr/bin/env python3
"""
Author : jayden <jayden@localhost>
Date   : 2023-08-26
Purpose: Rock the Casbah
"""

import argparse
import random
import re
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='File',
                        nargs="+",
                        help='Input file(s)',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--num',
                        metavar='num_passwords',
                        type=int,
                        help='Number of passwords to generate',
                        default=3)

    parser.add_argument('-w',
                        '--num_words',
                        metavar='num_words',
                        type=int,
                        help='Number of words to use for password',
                        default=4)

    parser.add_argument('-m',
                        '--min_word_len',
                        metavar='minimum',
                        help='Minimum word length',
                        type=int,
                        default=3)

    parser.add_argument('-x',
                        '--max_word_len',
                        metavar='maximum',
                        help='Maximum word length',
                        type=int,
                        default=6)
    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        help='Random seed',
                        type=int,
                        default=None)
    parser.add_argument('-l',
                        '--l33t',
                        help='Obfuscate letters',
                        action='store_true')

    return parser.parse_args()


def clean(word):
    """Remove whitespace and punctuation"""
    return re.sub('[^a-zA-Z0-9]', '', word)


def l33t(word):
    dic = {'a': '@', 'A': '4', 'O': '0', 't': '+', 'E': '3', 'I': '1', 'S': '5'}
    word = ransom(word)
    word = ''.join([dic.get(c, c) for c in word]) + random.choice(string.punctuation)
    return word


def ransom(word):
    """Randomly capitalize letters in a word"""
    return ''.join(
        map(lambda c: c.upper() if random.choice([0, 1]) else c.lower(), word))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    words = set()

    def word_len(word):
        return args.min_word_len <= len(word) <= args.max_word_len

    for fh in args.file:
        for line in fh:
            for word in filter(word_len, map(clean, line.lower().split())):
                words.add(word.title())

    words = sorted(words)
    # passwords = map(ransom, ["".join(random.sample(words, args.num_words)) for _ in range(args.num)])
    passwords = ["".join(random.sample(words, args.num_words)) for _ in range(args.num)]
    if args.l33t:
        passwords = map(l33t, passwords)
    print('\n'.join(passwords))


# --------------------------------------------------
if __name__ == '__main__':
    main()
