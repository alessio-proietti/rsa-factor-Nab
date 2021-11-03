#! /usr/bin/env python

import random
import libnum

n = 89855713
a = 82330933
b = 34986517

y = a*b - 1 

w = random.randint(1, n-1)
x = libnum.gcd(w, n)

if 1 < x < n:
    print("SUCCESS")


print(f"y = {y}, n = {n}, w = {w}, x = {x}")

if __name__ == "__main__":
    pass
