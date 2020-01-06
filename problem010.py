"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
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
    while primes[-1] < 2e6:
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

    return sum(primes) - primes[-1]

if __name__ == '__main__':
    sol = run()
    print(sol)
