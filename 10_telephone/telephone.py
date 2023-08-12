#!/usr/bin/env python3
"""
Author : jayden <jayden@localhost>
Date   : 2023-08-12
Purpose: Rock the Casbah
"""

import argparse
import os.path
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()
    if not 0 <= args.mutations <= 1:
        # if args.mutations < 0 or args.mutations > 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        # 读取文件内容
        args.text = open(args.text).read().rstrip()
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    nums_mutation = round(len(args.text) * args.mutations)
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))

    # new_text = ''
    # for char in args.text:
    #     new_text += random.choice(alpha) if random.random() <= args.mutations else char

    index_list = random.sample(range(len(args.text)), nums_mutation)
    new_text = args.text
    for item in index_list:
        new_text = new_text[:item] + random.choice(alpha.replace(new_text[item], '')) + new_text[item + 1:]

    print(f'You said: "{args.text}"')
    print(f'I heard : "{new_text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
