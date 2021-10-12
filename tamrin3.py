inporter = input('enter your date: ')
year, month, dey = inporter.split('/')

year = int(year)
month = int(month)
dey = int(dey)

dey += 1
range()

if dey >= 31 and month <= 6:
    dey = 1
    month += 1
elif dey >= 30 and month > 6:
    dey = 1
    month += 1
elif month > 12:
    month = 1
    year += 1

print(f'todey: {year}/{month}/{dey}')