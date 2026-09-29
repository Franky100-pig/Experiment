#!/usr/bin/env python3
"""Sieve of Eratosthenes — classic algorithm drill.

Date: 2026-09-29
Run: python3 main.py
"""
import math


def sieve(n: int):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.isqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i, p in enumerate(is_prime) if p]


def main() -> None:
    primes = sieve(50)
    print("primes <= 50:", primes)
    print("count:", len(primes))


if __name__ == "__main__":
    main()
