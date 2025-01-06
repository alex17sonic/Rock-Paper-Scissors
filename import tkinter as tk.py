menu = {"pizza margheritta" : 9.00,
        "pizza quatro formaggi" : 10.00,
        "pizza reginna" : 10.00,
        "pizza frutti di mare": 12.00,
        "Pizza Easter": 10.50,
        "cola": 2.50,
        "fanta": 2.50}

cart = []
total = 0

print("--------------------MENU--------------------")

for key, value in menu.items():
    print(f"{key:25}: \N{euro sign}{value:.2f}")

print("--------------------------------------------")

while True:
    food = input("Selecteaza comanda dorita, q sau Q pentru a iesi din menu:  ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print(cart)

print("------------Comanda Dumneavoastra--------------")

for food in cart:
    total = total + menu.get(food)
    print(food, end="  ")

print()
print(f"Total:\N{euro sign}{total:.2f}")