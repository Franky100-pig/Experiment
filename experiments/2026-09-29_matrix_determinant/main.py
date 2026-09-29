#!/usr/bin/env python3
"""Matrix determinant via Gaussian elimination (exact, no numpy).

Date: 2026-09-29
Ties into LA Helper's determinant module. Run: python3 main.py
"""
from fractions import Fraction


def determinant(matrix):
    n = len(matrix)
    a = [[Fraction(matrix[i][j]) for j in range(n)] for i in range(n)]
    det = Fraction(1)
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(a[r][col]))
        if a[pivot][col] == 0:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        det *= a[col][col]
        for r in range(col + 1, n):
            factor = a[r][col] / a[col][col]
            for c in range(col, n):
                a[r][c] -= factor * a[col][c]
    return det


def main() -> None:
    m = [
        [1, 2, 3],
        [0, 4, 5],
        [1, 0, 6],
    ]
    print("matrix:", m)
    print("det =", determinant(m))  # exact: 22


if __name__ == "__main__":
    main()
