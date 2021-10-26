class bsa(type):
    _instance = None

    def __call__(self, *args, **kwds):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance

class singleton(metaclass=bsa):
    pass

akbar = singleton()
asqar = singleton()

print(akbar is asqar)
print(id(akbar) == id(asqar))