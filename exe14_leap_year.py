""" As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.

Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year. """

""" Your task is to write and test a function which takes one argument (a year) and returns True if the year is a leap year, or False otherwise. """


def is_year_leap(year):
  if year < 1582:
    return 'Not in Gregorian calendar'
  if year % 4 != 0:
    return False
  if year % 100 != 0:
    return True
  if year % 400 != 0:
    return False
  else:
    return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")