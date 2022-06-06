import datetime

t = datetime.time(9, 20, 46, 1000)
# print(t)
# print(t.hour)

# datetime.day -> yr,month,day without time
# datetime.time -> hr,min,sec without day
dt = datetime.datetime(2019,4,13,12,45,21,351)  # both
# print(dt)
# print(dt.date())

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()  # gives option to pass timezone
dt_utcnow = datetime.datetime.utcnow()  # current utc time, it is not time zone aware date time


print(dt_today)
print(dt_now)
print(dt_utcnow)

