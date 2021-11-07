import datetime

past = datetime.date(2020,12,31)
now = datetime.date.today()
future = datetime.date(2021,12,31)

delta = (lambda p,n,f: f'прошло {p-n}, осталось {f-n}')(past, now, future)
print(delta)
