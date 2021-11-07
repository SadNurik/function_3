import datetime
now = datetime.datetime.now() - datetime.datetime(2021,1,1)
newyears = int(str(now).split()[0])
c = lambda days:365 - days
print(f'Прошло с нового года:',c(newyears),'дней '
