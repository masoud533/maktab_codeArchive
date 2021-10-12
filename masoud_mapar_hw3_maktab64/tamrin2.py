class book:

    def show_details(self):
        return f"{self.title} price: {self.price}, count: {self.count}"

    def __init__(self, title, price, count):
        self.title = title
        self.price = price
        self.count = count

book1 = book('Science', 100000, 10)
book2 = book('Math', 100000, 10)
book3 = book('Physics', 100000, 10)

print(book1.show_details())
print(book2.show_details())
print(book3.show_details()) 