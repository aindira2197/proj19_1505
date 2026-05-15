menu = {
    "Lavash": 25000,
    "Burger": 30000,
    "Pizza": 80000
}

total = 0

for food, price in menu.items():
    print(food, price)

while True:
    order = input("Taom nomi: ")

    if order == "stop":
        break

    if order in menu:
        total += menu[order]
        print("Qoshildi")
    else:
        print("Topilmadi")

print("Jami summa:", total)
