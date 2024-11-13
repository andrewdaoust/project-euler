"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def run():
    answer = None
    a = None
    b = None
    c = None
    for i in range(1, 334):
        if answer is not None:
            break
        upper = int((1000 - i) / 2)
        for j in range(i+1, upper):
            k = 1000 - (i + j)
            triplet = ((i ** 2) + (j ** 2) - (k ** 2)) == 0
            # print(i, j, k, triplet)
            if triplet:
                answer = i * j * k
                a = i
                b = j
                c = k
                break

    return answer

if __name__ == '__main__':
    sol = run()
    print(sol)
