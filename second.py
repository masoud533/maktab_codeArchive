second = int(input('enter second:'))
h = second // 360
second -= h*360
m = second // 60
second -= m*60
print(f'{h}:{m}:{second}')