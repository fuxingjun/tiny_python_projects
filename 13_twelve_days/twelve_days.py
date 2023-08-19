#!/usr/bin/env python3
"""
Author : jayden <jayden@localhost>
Date   : 2023-08-19
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='File',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    args = parser.parse_args()
    if args.num not in range(1, 13):
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


def verse(day):
    ordinal = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth',
               'eleventh', 'twelfth']
    gifts = ["And a partridge in a pear tree.",
             "Two turtle doves,",
             "Three French hens,",
             "Four calling birds,",
             "Five gold rings,",
             "Six geese a laying,",
             "Seven swans a swimming,",
             "Eight maids a milking,",
             "Nine ladies dancing,",
             "Ten lords a leaping,",
             "Eleven pipers piping,",
             "Twelve drummers drumming,"]
    if day == 1:
        return '\n'.join(
            ['On the first day of Christmas,', 'My true love gave to me,', 'A partridge in a pear tree.'])

    list1 = [f"On the {ordinal[day - 1]} day of Christmas,", "My true love gave to me,"]
    list1.extend(reversed(gifts[:day]))

    return '\n'.join(list1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # for day in range(1, args.num + 1):
    #     print(verse(day), file=args.outfile)

    print('\n\n'.join([verse(day) for day in range(1, args.num + 1)]), file=args.outfile)
    # create_file()
    # write_file()


def create_file():
    for i in range(1, 13):
        fh = open(f"./test-out/{i}.out", 'w')
        fh.close()


def write_file():
    for i in range(1, 13):
        print('\n\n'.join([verse(day) for day in range(1, i + 1)]), file=open(f"./test-out/{i}.out", 'w'))


# --------------------------------------------------
if __name__ == '__main__':
    main()


def test_verse():
    assert verse(1) == '\n'.join(
        ['On the first day of Christmas,', 'My true love gave to me,', 'A partridge in a pear tree.'])
    assert verse(2) == '\n'.join(
        ['On the second day of Christmas,', 'My true love gave to me,', 'Two turtle doves,',
         'And a partridge in a pear tree.'])
