"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from math import factorial

def run():
    n = str(factorial(100))
    summation = 0
    for i in range(len(n)):
        summation += int(n[i])

    return summation


if __name__ == '__main__':
    sol = run()
    print(sol)

