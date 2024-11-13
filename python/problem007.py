"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from math import sqrt

def is_new_prime(old_primes, potential_prime):
    # is_prime = True
    for prime in old_primes:
        if prime > sqrt(potential_prime):
            break
        if potential_prime % prime == 0:
            return False
    return True

def run():
    primes = [2, 3, 5, 7, 11, 13]

    n = 3
    while len(primes) < 10001:
        pp1 = 6 * n - 1
        pp2 = 6 * n + 1

        new1 = is_new_prime(primes, pp1)
        new2 = is_new_prime(primes, pp2)

        if new1:
            primes.append(pp1)
            # print(len(primes), ':', pp1)
        if new2:
            primes.append(pp2)
            # print(len(primes), ':', pp2)

        n += 1

    return primes[-1]

if __name__ == '__main__':
    sol = run()
    print(sol)
