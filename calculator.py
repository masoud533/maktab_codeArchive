while True:
     try:
       num1 = float(input('enter number1: '))
       num2 = float(input('enter number2: '))
     except ValueError:
        print("Oops!  That was no valid number.  Try again...")
action = input('inter action: ')

if action == '+':
    print(num1 + num2)
elif action == '-':
    print(num1 - num2)
elif action == '*':
    print(num1 * num2)
elif action == '/':
    print(num1 / num2)
else:
    print('somting wornt!')