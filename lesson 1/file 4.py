value_1 = input("Введите значение выручки фирмы: \n")
value_2 = input("Введите значение издержек фирмы: \n")

if value_1.isdigit() and value_2.isdigit():
    if value_1 > value_2 and value_2 != value_1:
        money = ((int(value_1) - int(value_2))/int(value_1))*100
        print("Компания работает с прибылью \n")
        print("Рентабельность выручки :", money)
        people = input("Введите численность рабочего штата: \n")
        money_for_person = money / int(people)
        print("Прибыль в расчете на сотрубника :", money_for_person)
    elif value_2 != value_1:
        print("Компания работает в убыток")
    elif value_2 == value_1:
        print("Компания вышла в '0'")
else:
    print("Значения явлюятся не целочисленным числом. Введите данные целочисленным числом")