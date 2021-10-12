num = int(input('enter number: '))
while num >= 10:
    list1 = []
    for i in repr(num):
        if i.isdigit():
            list1.append(int(i))
    num = sum(list1)
print(num)

