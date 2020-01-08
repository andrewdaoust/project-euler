"""
If the numbers 1 to 5 are written out in words: 
one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written 
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of 
"and" when writing out numbers is in compliance with British usage.
"""

def run():
    thousand = len('one') + len('thousand')

    # 1 -> 99: no 'hundred' (99)
    # 1000: no 'hundred' (1)
    # 1 + 99 = 100 w/o 'hundred' => 900 w/ 'hundred
    hundred = len('hundred') * 900

    # 1 -> 99: no 'and' (99)
    # 100, 200, ..., 900: no 'and' (9)
    # 1000: no 'and' (1)
    # 99 + 9 + 1 = 109 w/o 'and' => 891 w/ 'and'
    and_ = len('and') * 891

    # eleven: once every 100 -> 10 times
    # twelve: once every 100 -> 10 times
    # ...
    # nineteen: once every 100 -> 10 times
    # 10 * (len(eleven) + len(twelve) + ... + len(nineteen))
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    teens_len = 0
    for word in teens:
        teens_len += len(word)
    teens_len *= 10

    # 'one': 9 times per hundred in ones place -> 90 times
    #        100 times in the hundreds place -> 100
    #        => 190 times
    # 'two': 9 times per hundred in ones place -> 90 times
    #        100 times in the hundreds place -> 100
    #        => 190 times
    # etc.
    # 190 * (len(one) + len(two) + ... + len(nine))
    ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    ones_len = 0
    for word in ones:
        ones_len += len(word)
    ones_len *= 190
    
    # 'twenty': 10 times per hundred -> 100 times
    # 'thirty': 10 times per hundred -> 100 times
    # etc.
    # 100 * (len(twenty) + len(thirty) + ... + len(ninety))
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    tens_len = 0
    for word in tens:
        tens_len += len(word)
    tens_len *= 100

    total_sum = thousand + hundred + and_ + teens_len + ones_len + tens_len
    return total_sum


if __name__ == '__main__':
    sol = run()
    print(sol)
