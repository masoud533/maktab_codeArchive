class Add:
    list_1 = []
    def add(self, num) -> None:
        self.list_1.append(num)

mas = Add()

mas.add(1)
mas.add(2)
mas.add(3)
mas.add(4)
mas.add(5)

print(Add.list_1)