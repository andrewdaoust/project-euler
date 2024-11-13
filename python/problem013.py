"""
Work out the first ten digits of the sum of the following one-hundred
50-digit numbers. (See problem013.txt for list of numbers)
"""

def run():
    with open('inputs/problem013.txt') as f:
        nums = f.readlines()
        for i in range(len(nums)):
            nums[i] = int(nums[i])

        big_num = sum(nums)
        first_10 = str(big_num)[:10]
        return first_10


if __name__ == '__main__':
    sol = run()
    print(sol)