from datetime import date
def saturdays_between_two_dates(start, end):
    if start > end:
        start, end = end, start
    start_days = start.toordinal()
    end_days = end.toordinal()
    return sum(date.fromordinal(d).weekday() == 5 for d in range(start_days, end_days + 1)) 

date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))

for i in range(5):
    print(i**2)