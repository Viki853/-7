# Цены напитков
COFFEE_PRICE = 120
TEA_PRICE = 80
JUICE_PRICE = 100
WATER_PRICE = 50
LEMONADE_PRICE = 90

print("-" * 40)
print("             🌸МЕНЮ КАФЕ🌸")
print("-" * 40)
print("1. Кофе☕ - 120 рублей")
print("2. Чай🍵 - 80 рублей")
print("3. Сок🧃 - 100 рублей")
print("4. Вода🫗 - 50 рублей")
print("5. Лимонад🍹 - 90 рублей")

# Выбор напитка
drink_input = input("Введите номер напитка (1-5): ")

match drink_input:
    case "1":
        drink_name = "Кофе☕"
        price = COFFEE_PRICE
    case "2":
        drink_name = "Чай🍵"
        price = TEA_PRICE
    case "3":
        drink_name = "Сок🧃"
        price = JUICE_PRICE
    case "4":
        drink_name = "Вода🫗"
        price = WATER_PRICE
    case "5":
        drink_name = "Лимонад🍹"
        price = LEMONADE_PRICE
    case _:
        print("Ошибка: такого напитка нет")
        exit()

# Количество порций
try:
    quantity = int(input("Введите количество порций: "))
    if quantity <= 0:
        print("Ошибка: количество должно быть больше 0")
        exit()
except:
    print("Ошибка: введите число")
    exit()

# Скидки
discount = input("Введите код скидки (SUMMER, WELCOME или нажмите Enter чтобы пропустить): ")

match discount:
    case "SUMMER":
        discount_percent = 10
    case "WELCOME":
        discount_percent = 5
    case _:
        discount_percent = 0

# Расчет суммы
total = price * quantity
discount_amount = total * discount_percent / 100
final_total = total - discount_amount

if quantity == 1:
    portion_word = "порция"
elif 2 <= quantity <= 4:
    portion_word = "порции"
else:
    portion_word = "порций"

# Чек
print("\n" + "*" * 40)
print("        ✨ВАШ ЗАКАЗ✨")
print("*" * 40)
print(f"Напиток: {drink_name}")
print(f"Цена: {price} рублей")
print(f"Количество: {quantity} {portion_word}")
print(f"Сумма: {total} рублей")

if discount_percent > 0:
    print(f"Скидка: {discount_percent}%")
    print(f"Скидка: {discount_amount:.0f} рублей")

print(f"ИТОГО: {final_total:.0f} рублей")
print("_" * 40)