# Sam Cole
# 11/20/2019
from Person import Person


class Textbook:
    def __init__(self, title, first, last, age, edition, ISBN, publisher, publishyear, inventory, price):
        self.title = title
        self.author = Person(first, last, age)
        self.edition = edition
        self.ISBN = ISBN
        self.publisher = publisher
        self.publishyear = publishyear
        self.inventory = inventory
        self.price = price

    def addinv(self, addition):
        self.inventory = addition + self.inventory
        return self.inventory

    def subtractinv(self, subtraction):
        self.inventory = self.inventory - subtraction
        return self.inventory
