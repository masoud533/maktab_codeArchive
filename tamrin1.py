while True:
    try:
        num = int(input('please enter your fvorit number: '))
        break
    except ValueError:
        print('ops, There is a problem, please try again')

list1 = list(range(1, num+1))

for item in list1:
    print("*" * item)
for item in list1[len(list1)-2::-1]:
    print("*" * item)


