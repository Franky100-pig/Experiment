#!/usr/bin/env python3
"""ASCII Mandelbrot — zero-dependency daily experiment.

Date: 2026-09-29

Renders the Mandelbrot set as ASCII art using only the standard library.
Run: python3 main.py
"""
CHARS = " .:-=+*#%@"


def mandelbrot(c: complex, max_iter: int = 30) -> int:
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter


def render(width: int = 80, height: int = 24) -> None:
    for y in range(height):
        row = ""
        for x in range(width):
            re = -2.0 + (x / width) * 3.0
            im = -1.2 + (y / height) * 2.4
            m = mandelbrot(complex(re, im))
            row += CHARS[m * (len(CHARS) - 1) // 30]
        print(row)


if __name__ == "__main__":
    render()
