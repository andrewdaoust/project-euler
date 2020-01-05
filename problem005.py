"""2520 is the smallest number that can be divided by each 
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?"""

primes = [2, 3, 5, 7, 11, 13, 17, 19]

n2 = [2]
n3 = [3]
n4 = [2, 2]
n5 = [5]
n6 = [2, 3]
n7 = [7]
n8 = [2, 2, 2]
n9 = [3, 3]
n10 = [2, 5]
n11 = [11]
n12 = [2, 2, 3]
n13 = [13]
n14 = [2, 7]
n15 = [3, 5]
n16 = [2, 2, 2, 2]
n17 = [17]
n18 = [2, 3, 3]
n19 = [19]
n20 = [2, 2, 5]

factorizations = [n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20]
counts = [0, 0, 0, 0, 0, 0, 0, 0]

for fac in factorizations:
    for i in range(len(primes)):
        c = fac.count(primes[i])
        if c > counts[i]:
            counts[i] = c

# smallest_multiple = 1 * (2 ** 4) * (3 ** 2) * 5 * 7 * 11 * 13 * 17 * 19
smallest_multiple = 1 * (2 ** counts[0]) * (3 ** counts[1]) * (5 ** counts[2]) * (7 ** counts[3]) * (
    11 ** counts[4]) * (13 ** counts[5]) * (17 ** counts[6]) * (19 ** counts[7])

print(smallest_multiple)
