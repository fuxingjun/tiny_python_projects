#!/usr/bin/env python3
"""
Author : jayden <jayden@localhost>
Date   : 2023-08-28
Purpose: Rock the Casbah
"""

import argparse
import re
import sys
from typing import List, NamedTuple, Optional


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--board',
                        help='The state of the board',
                        metavar='str',
                        type=str,
                        default='.' * 9)

    parser.add_argument('-p',
                        '--player',
                        help='Player',
                        choices='XO',
                        metavar='player',
                        type=str,
                        default=None)

    parser.add_argument('-c',
                        '--cell',
                        help='Cell 1-9',
                        metavar='cell',
                        type=int,
                        choices=range(1, 10),
                        default=None)
    args = parser.parse_args()

    if any([args.player, args.cell]) and not all([args.player, args.cell]):
        parser.error('Must provide both --player and --cell')

    if not re.search('^[.XO]{9}$', args.board):
        parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')

    if args.player and args.cell and args.board[args.cell - 1] in 'XO':
        parser.error(f'--cell "{args.cell}" already taken')

    return args


class State(NamedTuple):
    board: List[str] = list('.' * 9)
    player: str = 'X'
    quit: bool = False
    draw: bool = False
    error: Optional[str] = None
    winner: Optional[str] = None


def format_board(board: List[str]) -> str:
    cells = [str(i) if c == '.' else c for i, c in enumerate(board, start=1)]
    bar = '-------------'
    cells_template = '| {} | {} | {} |'

    return '\n'.join([
        cells_template.format(*cells[:3]), bar,
        cells_template.format(*cells[3:6]), bar,
        cells_template.format(*cells[6:9]), bar,
    ])


def find_winner(board: List[str]) -> Optional[str]:
    winning = [
        [0, 1, 2],  # across the top
        [3, 4, 5],  # across the middle
        [6, 7, 8],  # across the bottom
        [0, 3, 6],  # down the left
        [1, 4, 7],  # down the middle
        [2, 5, 8],  # down the right
        [0, 4, 8],  # diagonal
        [2, 4, 6],  # diagonal
    ]

    for player in 'XO':
        for i, j, k in winning:
            combo = [board[i], board[j], board[k]]
            if combo == [player, player, player]:
                return player

    return None


def get_move(state: State) -> State:
    move = input(f'Player {state.player}, what is your move? [q to quit]:')
    if move == 'q':
        sys.exit('You lose, loser!')
    if not re.match('^[1-9]$', move):
        return state._replace(error=f'Invalid cell "{move}", please choose 1-9')
    if state.board[int(move) - 1] in 'XO':
        return state._replace(error=f'Cell "{move}" already taken')
    board = state.board[:]
    board[int(move) - 1] = state.player
    winner = find_winner(board)
    if winner:
        return state._replace(board=board, winner=winner)
    if '.' not in board:
        return state._replace(board=board, draw=True)
    return state._replace(board=board, player='O' if state.player == 'X' else 'X')


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    state = State()
    while True:
        print(format_board(state.board))
        state = get_move(state)
        if state.winner:
            print(format_board(state.board))
            print(f'Player {state.winner} has won!')
            break
        if state.error:
            print(state.error)
        if state.draw:
            print('Draw!')
            break


# --------------------------------------------------
if __name__ == '__main__':
    main()
