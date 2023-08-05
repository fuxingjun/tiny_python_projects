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
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    item_arg = args.item
    bool_sort = args.sorted

    str_len = len(item_arg)

    if bool_sort:
        item_arg.sort()

    str_prefix = 'You are bringing'
    if str_len < 2:
        formatted_string = item_arg[0]
    elif str_len == 2:
        formatted_string = f'{item_arg[0]} and {item_arg[1]}'
    else:
        item_arg[-1] = 'and ' + item_arg[-1]
        formatted_string = f'{", ".join(item_arg)}'

    print(f'{str_prefix} {formatted_string}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
