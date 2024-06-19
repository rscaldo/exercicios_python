""" Your task is to write and test a function which takes two arguments (a year and a month) and returns the number of days for the given year-month pair (while only February is sensitive to the year value, your function should be universal). """

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



def days_in_month(year,month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #converte o índice de 1 a 12
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

test_years = [1900, 2000, 2016, 1987]
test_months = [ 2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr,mo,"-> ",end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
