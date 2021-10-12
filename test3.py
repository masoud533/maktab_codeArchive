num = int(input('enter your number: '))

x = 1
for a in range(1, num+1):
    for i in range(1, num+1):
        print(i * x, end='\t')
    print()
    x += 1

