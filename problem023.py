"""
A perfect number is a number for which the sum of its proper divisors 
is exactly equal to the number. For example, the sum of the proper 
divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 
is a perfect number.

A number n is called deficient if the sum of its proper divisors is 
less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the 
smallest number that can be written as the sum of two abundant 
numbers is 24. By mathematical analysis, it can be shown that all 
integers greater than 28123 can be written as the sum of two abundant 
numbers. However, this upper limit cannot be reduced any further by 
analysis even though it is known that the greatest number that 
cannot be expressed as the sum of two abundant numbers is less than 
this limit.

Find the sum of all the positive integers which cannot be written as 
the sum of two abundant numbers.
"""

from math import sqrt
from itertools import combinations_with_replacement as cwr  # Use this or combo?


def factorize(n):
    factors = [1]
    if n % 2 == 0:
        r = range(2, int(sqrt(n)))
    else:
        r = range(3, int(sqrt(n)), 2)

    for i in r:
        if n % i == 0:
            f = int(n / i)
            factors.append(i)
            if f != i:
                factors.append(f)
    return factors


def abundant(n, factors):
    factors_sum = sum(factors)
    return True if n < factors_sum else False


def deficient(n, factors):
    factors_sum = sum(factors)
    return True if n > factors_sum else False


def perfect(n, factors):
    factors_sum = sum(factors)
    return True if n == factors_sum else False


def run():
    abundant_nums = []
    for i in range(12, 28123):
        f = factorize(i)
        is_abundant = abundant(i, f)
        if is_abundant:
            abundant_nums.append(i)

    combos = cwr(abundant_nums, 2)
    abundant_sums = []
    for combo in combos:
        abundant_sums.append(sum(combo))

    summation = 0
    for n in range(1, 28123):
        if n not in abundant_sums:
            summation += n

    return summation


if __name__ == '__main__':
    sol = run()
    print(sol)
