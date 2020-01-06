"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import numpy as np

def prime_check(num):
    if num % 2 == 0:
        return False
    n1 = (num - 1) % 6 == 0
    n2 = (num + 1) % 6 == 0

    return n1 or n2

def factors(num):
    n = int(np.sqrt(num))
    facs = []
    p = False
    while n > 0:
        # print(n)
        if num % n == 0:
            facs.append(n)
        n -= 1

    return facs

def run():
    facs = factors(600851475143)

    max_factor = 0
    for fac in facs:
        f = factors(fac)
        if len(f) == 1:
            return fac

if __name__ == '__main__':
    sol = run()
    print(sol)
