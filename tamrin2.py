string1 = list(input('enter your string: ').strip(' '))
string2 = ['a', 'o', 'u', 'e', 'i', ' ']
Output = ""
for item in string1:
    for value in string2:
        if value in string1:
            string1.remove(value)
for item in string1:
    Output += item+'.'
print(Output)

