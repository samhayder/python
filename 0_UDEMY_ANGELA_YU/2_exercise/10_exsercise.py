# Find Leap year
def is_leap_year(year):
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        print(True)
    else:
        print(False)

#is_leap_year(2400)
is_leap_year(100)