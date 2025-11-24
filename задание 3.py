from unittest import case

print( " -----------------------------------------------------")
print(  " ---              МЕНЮ  КАФЕ                       --- ")
print( " -----------------------------------------------------")
print("1 Кофе - 120 руб")
print("2 Чай - 80 руб")
print("3 Сок - 100 руб")
print("4 Вода - 50 руб")
print("5 Лимонад - 90 руб")
while True:
    n= input("Выберите номер напитка (1-5): ")
    match n:
         case "1":
             drink= "Кофе"
             price= 120

         case "2":
             drink= "Чай"
             price= 80

         case "3":
             drink = "Сок"
             price = 100

         case "4":
             drink = "Вода"
             price = 50

         case "5":
             drink = "Лимонад"
             price = 90
         case _:
             print(" Ошибка. Введите число от 1 до 5")

while type:
    try:
        k= int(input("Сколько порций?"))
        if k >0:
            eval("Число должно быть больше нуля")
print("Введите число")
s=input("Усть скидка? : ")







