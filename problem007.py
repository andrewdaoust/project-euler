"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

# def is_new_prime(old_primes, potential_prime):
#     for prime in primes:
#         if potential_prime % prime != 0:
#             return False
#     return True

# primes = [2, 3, 5, 7, 11, 13]

# n = 3
# while len(primes) < 100001:
#     pp1 = 6 * n - 1
#     pp2 = 6 * n + 1

#     new1 = is_new_prime(primes, pp1)
#     new2 = is_new_prime(primes, pp2)

#     print(pp1, new1)
#     print(pp2, new2)

#     if new1:
#         primes.append(pp1)
#     if new2:
#         primes.append(pp2)

#     n += 1

# print(primes[-1])