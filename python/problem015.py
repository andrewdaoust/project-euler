"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the
right and down, there are exactly 6 routes to the bottom right corner. (Example image
in the 'inputs' folder)

How many such routes are there through a 20×20 grid?
"""

from math import factorial


def binomial_coefficient(n, k):
    n_fac = factorial(n)
    if n == k:
        k_fac = n_fac
        n_diff_k_fac = 1
    else:
        k_fac = factorial(k)
        n_diff_k_fac = factorial(n - k)

    return int(n_fac / (k_fac * n_diff_k_fac))

def run():
    n = 20
    k = 20
    paths = binomial_coefficient(n + k, n)
    return paths


if __name__ == '__main__':
    sol = run()
    print(sol)
