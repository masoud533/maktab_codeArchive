import random
num_min = 1
num_max = 99
while True:
    num = random.randint(num_min, num_max)
    print(f'Do you think: {num}')
    while True:
        value = input('Tell us your opinion(d for True, b for Bigger, k for Smaller): ')
        if value == 'k' or value =='b' or value == 'd':
            break
    if value == 'k':
        num_max = num - 1
    elif value == 'b':
        num_min = num + 1
    else:
        break
print(f'you think: {num}')

