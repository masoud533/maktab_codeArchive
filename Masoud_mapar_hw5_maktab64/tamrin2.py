class bsa(type):
    _instance = None

    def __call__(self, *args, **kwds):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance

class Add(metaclass=bsa):
    list_1 = []
    def add(self, num) -> None:
        self.list_1.append(num)        

    def plus(self):
        return sum(self.list_1)



mas = Add()
while True:
    try:
        key = input('for exit press * for add number, enter number:')
        if key == '*':
            break
        elif type(int(key)) == type(1):
            x = int(key) + 1
            mas.add(int(key))
    except ValueError:
        print('error')
    except TypeError:
        print('error')

print(mas.plus())