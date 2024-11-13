"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting
numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def even(n):
    return int(n / 2)


def odd(n):
    return 3 * n + 1


def run():
    longest_chain = 0
    num = 1
    for i in range(1, 1000000):
        n = i
        chain = 1
        while n != 1:
            if n % 2 == 0:
                n = even(n)
            else:
                n = odd(n)

            chain += 1

        if chain > longest_chain:
            longest_chain = chain
            num = i

    return '{0} has the logest chain with {1} steps'.format(num, longest_chain)


if __name__ == '__main__':
    sol = run()
    print(sol)