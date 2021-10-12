import time
class age:
    def year_old(self):
        t = (self.year, self.month, self.day, 0, 0, 0, 0, 0, 0)
        t = time.mktime(t)
        t2 = time.time()
        time_1 = t2 - t 
        y = int(time_1 // 31104000)
        return f' you are: {y} yearsold'

    def hour(self):
        t = (self.year, self.month, self.day, 0, 0, 0, 0, 0, 0)
        t = time.mktime(t)
        t2 = time.time()
        time_1 = t2 - t 
        h = int(time_1 // 3600)
        return f'  You lived {h} hours'

    def Until_birth(self):
        t = (self.year, self.month, self.day, 0, 0, 0, 0, 0, 0)
        t = time.mktime(t)
        t2 = time.time()
        time_1 = t2 - t
        y = int(time_1 // 31104000) + 1
        t3 = (self.year + y, self.month, self.day, 0, 0, 0, 0, 0, 0)
        t3 = time.mktime(t3)
        time_1 = t2 - t3
        time_1 = abs(time_1)
        m = int(time_1 // 2592000)
        time_1 -= m*2592000
        d = int(time_1 // 21600)
        time_1 -= d*21600
        h = int(time_1 // 3600) 
        time_1 -= h*3600
        time_1 = int(time_1)
        return f'   {m} month {d} day {h} hour {time_1} second  left until your birthday'
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

while True:
    try:
       year =  int(input('Enter your year of birth: '))
       month =  int(input('Enter your month of birth: '))
       dey =  int(input('Enter your dey of birth: '))
       break
    except TypeError:
        print('ops, enter valid value!')

print(age(year, month, dey).year_old())
print(age(year, month, dey).hour())
print(age(year, month, dey).Until_birth()) 
