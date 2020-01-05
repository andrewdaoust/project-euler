"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def palindrome_check(n):
    s = str(n)
    length = len(s)

    for i in range(int(len(s)/2)):
        j = -i - 1
        if s[i] != s[j]:
            return False
    return True

palindrome_numbers = []
for i in range(999, 99, -1):
    palindrome = False
    for j in range(i, 99, -1):
        num = i * j
        palindrome = palindrome_check(num)
        print(i, j, num, palindrome)
        if palindrome:
            palindrome_numbers.append(num)
    
print(max(palindrome_numbers))
