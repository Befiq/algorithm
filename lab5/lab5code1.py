num = []
l = int(input("Введите кол-во чисел которые вы хотите доавить: "))



for i in range(l):
    n = int(input("Введите числа: "))
    num.append(n)


if l <= 0:
    print("Числа не могут быть отрицатеьными!!!")
else:
    print(num)