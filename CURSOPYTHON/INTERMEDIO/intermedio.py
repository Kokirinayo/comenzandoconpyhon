#date

from datetime import datetime

fecha = datetime(201, 1, 12, 9, 12,12)

print(fecha.second)

now = datetime.now()

print(now)

print(now.minute)

from datetime import time

my_time = time(3, 45)

print(my_time.minute)

from datetime import date

my_date = date.today()
print(my_date)

new_year = datetime(2025, 4, 12)
print(new_year - now)