num = int(input('enter your number: '))
list = []
for i in range(1,11):
    num2 = i * num
    print(f'{num} * {i} = {num2}')
    list.append(num2)
print(list)
