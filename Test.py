# Sam Cole
# 11/20/2019
from Textbook import Textbook


Text1 = Textbook("Life in the universe", "Jefferey", "Bennett", 34, 4, 9780134089089, "Pearson", 2017, 26, 203)
Text2 = Textbook("The Best Day", "Bob", "Dylan", 56, 2, 8621453765412, "Best-men", 2018, 7, 345)
print("Hello you have 2 different Textbooks in your inventory.")
print(Text1.title + " and there is " + str(Text1.inventory) + " in inventory")
print("Has the price or inventory changed with this textbook?"
      "If so enter price or inventory ")
answer = input()
if answer == "inventory":
    print("subtract or add?")
    answer1 = input()
    if answer1 == "subtract":
        print("By how much?")
        answer2 = int(input())
        if Text1.subtractinv(answer2) < 0:
            print("I'm sorry that would bring the inventory below zero")
        else:
            Text1.subtractinv(answer2)
            print("The inventory is now " + str(Text1.inventory))
    elif answer1 == "add":
        print("By how much?")
        answer2 = int(input())
        Text1.addinv(answer2)
        print("The inventory is now " + str(Text1.inventory))
elif answer == "price":
    print("What is the new price")
    price = input()
    Text1 = Textbook("Life in the universe", "Jefferey", "Bennett", 34, 4, 9780134089089, "Pearson", 2017, 26, price)
    print("The price is now " + str(Text1.price))
else:
    print("OK")
print(Text2.title + " and there is " + str(Text2.inventory) + " in inventory")
print("Has the price or inventory changed with this textbook?"
      "If so enter price or inventory ")
answer3 = input()
if answer3 == "inventory":
    print("subtract or add?")
    answer1 = input()
    if answer1 == "subtract":
        print("By how much?")
        answer2 = int(input())
        Text1.subtractinv(answer2)
        print("The inventory is now " + str(Text1.inventory))
    elif answer1 == "add":
        print("By how much?")
        answer2 = int(input())
        if Text2.addinv(answer2) < 0:
            print("I'm sorry that would bring the inventory below zero")
        else:
            Text2.addinv(answer2)
            print("The inventory is now " + str(Text1.inventory))
elif answer3 == "price":
    print("What is the new price")
    price = input()
    Text2 = Textbook("The Best Day", "Bob", "Dylan", 56, 2, 8621453765412, "Best-men", 2018, 7, price)
    print("The price is now " + str(Text2.price))
