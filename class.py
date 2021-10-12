class Car:

    def __init__(self, name, numberOfDor, color):
        self.name = name
        self.numberOfDor = numberOfDor
        self.color = color

benz = Car('sls', 2, 'red')

print(benz.color)