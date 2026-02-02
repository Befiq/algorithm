#Простой калькулятор (доп задача)
chislo_1 = int(input("Введите число:"))
operat = input("Введиет операцию:")
chislo_2 = int(input("Введите число:"))

if operat == "+":
    print("Ответ:",chislo_1 + chislo_2)

elif operat == "-":
    print("Ответ:",chislo_1 - chislo_2)

elif operat == "/":
    print("Ответ:",chislo_1 // chislo_2)

elif operat == "*":
    print("Ответ:",chislo_1 * chislo_2)

elif operat == "^":
    print("Ответ:",chislo_1 ** chislo_2)

else:
    print("Вы ввели недопустимое значение !ОШИБКА!")
