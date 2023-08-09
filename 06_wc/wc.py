#!/usr/bin/env python3
"""
Author : jayden <jayden@localhost>
Date   : 2023-08-09
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs="*",
                        help='Input file(s)',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    parser.add_argument('-l', '--line', help='line flag', action='store_true', default=False)
    parser.add_argument('-w', '--word', help='word flag', action='store_true', default=False)
    parser.add_argument('-c', '--char', help='char flag', action='store_true', default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.file

    # 如果没有传入输出配置，那么默认输出所有的
    if not args.line and not args.word and not args.char:
        args.line, args.word, args.char = True, True, True

    template = '{num_lines:8}{num_words:8}{num_chars:8} {name}'
    total_template = '{total_lines:8}{total_words:8}{total_chars:8} total'
    if not args.line:
        template = template.replace('{num_lines:8}', '')
        total_template = total_template.replace('{total_lines:8}', '')
    if not args.word:
        template = template.replace('{num_words:8}', '')
        total_template = total_template.replace('{total_words:8}', '')
    if not args.char:
        template = template.replace('{num_chars:8}', '')
        total_template = total_template.replace('{total_chars:8}', '')

    # total_lines = 0
    # total_words = 0
    # total_chars = 0
    total_lines, total_words, total_chars = 0, 0, 0
    for fh in file:
        num_lines = 0
        num_words = 0
        num_chars = 0
        for line in fh:
            # read each line
            num_lines += 1
            num_words += len(line.split())
            num_chars += len(line)
        total_lines += num_lines
        total_words += num_words
        total_chars += num_chars
        # print(f'{num_lines:8}{num_words:8}{num_chars:8} {fh.name}')
        print(template.format(num_lines=num_lines, num_words=num_words, num_chars=num_chars, name=fh.name))
    if len(file) > 1:
        print(total_template.format(total_lines=total_lines, total_words=total_words, total_chars=total_chars))


# --------------------------------------------------
if __name__ == '__main__':
    main()
