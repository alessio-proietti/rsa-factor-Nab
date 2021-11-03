#! /usr/bin/env python

import random
import libnum


def square_and_multiply(x, c, n):
    c = bin(c)
    z = x

    for i in range(3, len(c)):
        z = z ** 2 % n
        if c[i:i+1] == '1':
            z = z * x % n

    return z


def highest_power_of_two(mphi):
    s = 0
    d = mphi

    while (d & 1 == 0):
        s += 1
        d = (d >> 1)

    pwt = 2 ** s
    r = mphi // pwt

    return s, r


def factoring(n, a, b):

    mphi = a*b - 1

    s, r = highest_power_of_two(mphi)

    w = random.randint(1, n-1)

    x = libnum.gcd(w, n)

    if 1 < x < n:
        print(f"SUCCESS, factor = {x}.")
        return "SUCCESS", x

    v = square_and_multiply(w, r, n)

    if (v % n == 1):
        print("FAILURE. Please rerun.")
        return "FAILURE", -11

    v_0 = None

    while (v % n != 1):
        v_0 = v
        v = (v**2) % n

    if (v_0 % n == -1):
        print("FAILURE. Please rerun.")
        return "FAILURE", -11
    else:
        x = libnum.gcd(v_0+1, n)
        print(f"SUCCESS, factor = {x}.")
        return "SUCCESS", x


if __name__ == "__main__":

    n = 89855713
    a = 82330933
    b = 34986517

    print(f"\nWe know a = {a}, b = {b}.")
    print(f"We want to use them to factor n = {n}.")
    status, factor = factoring(n, a, b)

    if status == "SUCCESS":
        other_factor = n // factor
        print(f"\nIt seems that {factor} * {other_factor} = {n}")
        
        if factor == n:
            print("TRIVIAL FACTOR. Found factor equals n.")
