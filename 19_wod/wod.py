#!/usr/bin/env python3
"""
Author : jayden <jayden@localhost>
Date   : 2023-08-26
Purpose: Rock the Casbah
"""

import argparse
import csv
import io
import random
from pprint import pprint
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='Seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='exercise',
                        type=int,
                        default=4)

    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')

    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


def read_csv(fh):
    reader = csv.DictReader(fh, delimiter=',')
    exercises = []
    for rec in reader:
        name, reps = rec['exercise'], rec['reps']
        low, high = reps.split("-")
        exercises.append((name, int(low), int(high)))
    return exercises


def test_read_csv():
    text = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(text) == [('Burpees', 20, 50), ('Situps', 40, 100)]


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    def helper(x):
        return x[0], int(random.randint(x[1], x[2]) / (2 if args.easy else 1))

    exercises = list(map(helper, random.sample(read_csv(args.file), args.num)))

    print(tabulate(exercises, headers=('Exercise', 'Reps')))


# --------------------------------------------------
if __name__ == '__main__':
    main()
