from datetime import date, datetime, timedelta
import locale

today = date.today()
# date
print(today) # 2022-10-19
print(today.day) # 19
print(today.month) # 10
print(today.year) # 2022
print(today.weekday()) # 2

# datetime
locale.setlocale(locale.LC_ALL, 'ru_RU')

now = datetime.today() # 2022-10-19 08:50:47.560832
now2 = datetime.now() # 2022-10-19 08:50:47.560832

print(now, now2, sep='\n')
print(now.hour)
print(now.second)
print(now.minute)


print(now.strftime('%a')) # Wed
print(now.strftime('%A')) # Wednesday

print(now.strftime('%A, %d %b %Y')) # среда, 19 окт 2022
print(now.strftime('%H %M %S')) # 09 15 01
print(now.strftime('%c')) # 19.10.2022 9:15:40
print(now.strftime('%x')) # 19.10.2022
print(now.strftime('%X')) # 9:15:40


print(now) # 2022-10-19 09:18:30.559074
print(now + timedelta(days=1, hours=2, minutes=3)) # 2022-10-20 11:21:30.559074







