"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import numpy as np

def run():
    mult_3_5 = []
    for i in range(1, 1000):
        if i % 3 == 0:
            mult_3_5.append(i)
        elif i % 5 == 0:
            mult_3_5.append(i)

    sol = np.sum(mult_3_5)
    return sol

if __name__ == '__main__':
    sol = run()
    print(sol)
