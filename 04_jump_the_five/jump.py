#!/usr/bin/env python3
"""
Author : jayden <jayden@localhost>
Date   : 2023-08-05
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    dic = {
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5',
    }

    # source = args.str
    # result = ''
    # for item in source:
    #     result += dic.get(item, item)
    # print(result)

    # source = list(args.str)
    # for index, value in enumerate(source):
    #     if dic.get(value) is not None:
    #         source[index] = dic.get(value)
    #
    # print(''.join(source))

    # for char in args.str:
    #     print(dic.get(char, char), end='')

    # print(''.join([dic.get(char, char) for char in args.str]), end='')

    print(args.str.translate(str.maketrans(dic)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
