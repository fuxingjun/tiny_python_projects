#!/usr/bin/env python3
"""
Author : jayden <jayden@localhost>
Date   : 2023-08-06
Purpose: Rock the Casbah
"""

import argparse
import io
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='outfile',
                        help='Output filename',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    outfile = args.outfile

    if os.path.isfile(text):
        text = open(text)
    else:
        text = io.StringIO(text + '\n')

    # if outfile:
    #     out_fh = open(outfile, 'wt')
    #     out_fh.write(text.upper())
    #     out_fh.close()
    # else:
    #     print(text.upper())

    out_fh = open(outfile, 'wt') if outfile else sys.stdout
    # out_fh.write(text.upper())
    for line in text:
        out_fh.write(line.upper())
    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
