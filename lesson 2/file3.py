"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""


"""dict variant"""
seasons = {
    12: "зима",
    1: "зима",
    2: "зима",
    3: "весна",
    4: "весна",
    5: "весна",
    6: "лето",
    7: "лето",
    8: "лето",
    9: "осень",
    10: "осень",
    11: "осень"
    }
number = int(input("Введите номер месяца \n"))
number = seasons.get(number)
print(number)


"""list variant"""
list = [None,"зима","зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
number = int(input("Введите номер месяца \n"))
number = list[number]
print(number)