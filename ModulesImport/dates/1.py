import datetime

d = datetime.date(2019, 9, 20)
# print(d)

tday = datetime.date.today()
# print(tday)
# print(tday.year)
# print(tday.day)
# print(tday.weekday())  # mon: 0, sun: 6
# print(tday.isoweekday())  # mon: 1, sun: 7

tdelta = datetime.timedelta(days=7)
# print(tdelta)
# print(tday + tdelta)

# note:-
# if we add/sub timedelta from date, we get date
# if we add/sub time from date, we get timedelta
# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2023, 4, 1)
till_bday = bday - tday
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())


