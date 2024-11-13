"""The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
"""

def run():
    nums = list(range(1, 101))

    sum_squared = sum(nums) ** 2

    squares_summed = 0
    for i in nums:
        squares_summed += i ** 2

    return sum_squared - squares_summed

if __name__ == '__main__':
    sol = run()
    print(sol)
