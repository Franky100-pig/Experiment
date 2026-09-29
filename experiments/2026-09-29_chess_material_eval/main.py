#!/usr/bin/env python3
"""Tiny chess material evaluator.

Date: 2026-09-29
Ties into Psyches (chess AI). Given a board as a string of piece letters
(uppercase = White, lowercase = Black, '.' = empty), return the material score
from White's perspective (positive = White ahead). Run: python3 main.py
"""
VALUES = {
    "P": 1, "N": 3, "B": 3, "R": 5, "Q": 9, "K": 0,
    "p": -1, "n": -3, "b": -3, "r": -5, "q": -9, "k": 0,
}


def material_score(board: str) -> int:
    return sum(VALUES.get(p, 0) for p in board)


def main() -> None:
    # starting position flattened rank8..rank1 (64 squares)
    board = "rnbqkbnr" "pppppppp" "........" "........" \
            "........" "........" "PPPPPPPP" "RNBQKBNR"
    print("starting position material:", material_score(board))  # 0
    board = board[:0] + "." + board[1:]  # Black loses a rook (a8)
    print("after Black loses a rook:", material_score(board))     # +5


if __name__ == "__main__":
    main()
