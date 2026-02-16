num = []
l = int(input("Введите кол-во чисел которое вы хотите ввести в список: "))

for i in range(l):
    n = int(input("Введите числа: "))
    num.append(n)

x = int(input())

found = False

for i in range(len(num)):
    if num[i] == x:
        print("Найдено,индекс:", i)
        found = True
        break
    if not found:
      print("Число не найдено")