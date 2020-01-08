"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def run():
    digits = str(2 ** 1000)
    summation = 0
    for i in range(len(digits)):
        n = int(digits[i])
        summation += n

    return summation


if __name__ == '__main__':
    sol = run()
    print(sol)