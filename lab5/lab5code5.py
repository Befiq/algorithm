num = []
l = int(input("Введите кол-во чисел которое вы хотите ввести в список: "))


for i in range(l):
    n = int(input("Введите числа: "))
    num.append(n)
    if l < 2:
        print("Недостаточно элементов")
        break

    else:
      max1 = num[0]
      max2 = num[0]

for i in range(1, l):
    if num[i] > max1:
        max2 = max1
        max1 = num[i]
    elif num[i] > max2 and num[i] != max1:
        max2 = num[i]

if max1 == max2:
    print("Второго по величине нет")
else:
    print(max2)