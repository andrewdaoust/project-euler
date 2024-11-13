"""
Let d(n) be defined as the sum of proper divisors of n (numbers less 
than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable
pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 
20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 
284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def d(n):
    if n == 1:
        return 0
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)

    return sum(factors)


def run():
    n = 10000
    amicable_nums = []
    for i in range(1, n):
        if i in amicable_nums:
            continue
        possible_amicable_num = d(i)
        if i != possible_amicable_num:
            if i == d(possible_amicable_num):
                amicable_nums.append(i)
                amicable_nums.append(possible_amicable_num)

    return sum(amicable_nums)


if __name__ == '__main__':
    sol = run()
    print(sol)
