chislo = int(input("Введите число:"))


if chislo % 3 == 0 and chislo % 5 == 0:
    print("Число делиться на 3 и 5")

elif chislo % 3 != 0 and chislo %5 == 0:
    print("Число делиться только на 5")

elif chislo % 5 != 0 and chislo %3 == 0:
    print("Число делиться только на 3")

else:
    print("Число не делится на 5 и 3")