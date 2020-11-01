from datetime import datetime
from datetime import timedelta


date = datetime(1901, 1, 1)
day = timedelta(days=1)
first_sundays = 0
firsts = 0
while date <= datetime(2000, 12, 31):
    if date.strftime('%d') == '01':
        firsts += 1
        if date.strftime('%w') == '0':
            first_sundays += 1
    date += day
print(firsts)
print(first_sundays)
