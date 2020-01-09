"""
You are given the following information, but you may prefer to do 
some research for yourself.

* 1 Jan 1900 was a Monday.
* Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
* A leap year occurs on any year evenly divisible by 4, 
  but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the 
twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def next_month_start(this_month_start, num_days):
    days = ["Su", "M", "T", "W", "R", "F", "Sa"]
    i = days.index(this_month_start)
    extra_days = (i + num_days) % 7
    
    return days[extra_days]


def run():
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    start = 'T'

    sunday_starts = 0
    for year in range(1901, 2001):
        extra_day = True if year / 4 == 0 else False

        for i in range(len(months)):
            days = months[i]
            if (i == 1) and extra_day:
                days += 1

            start = next_month_start(start, days)
            if start == 'Su':
                sunday_starts += 1

    return sunday_starts


if __name__ == '__main__':
    sol = run()
    print(sol)
