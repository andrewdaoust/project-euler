"""
Using names.txt, a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its alphabetical position in 
the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, 
COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def run():
    with open('inputs/names.txt') as f:
        names = f.readline().replace('"', '').split(',')

    names.sort()
    score = 0
    for i in range(len(names)):
        place = i + 1
        name = names[i]
        name_score = 0
        for letter in name:
            name_score += ord(letter) - 64
        name_score *= place
        score += name_score
    return score


if __name__ == '__main__':
    sol = run()
    print(sol)
