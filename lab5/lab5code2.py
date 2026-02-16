numbers = []
n = int(input("Введите кол-во чисел которое вы хотите ввести в список: "))

for i in range(n):
    a = int(input())
    numbers.append(a)

total = 0
maximum = numbers[0]
minimum = numbers[0]

for f in range(len(numbers)):
    total += numbers[f]

    if numbers[f] > maximum:
        maximum = numbers[f]

    if numbers[f] < minimum:
        minimum = numbers[f]

avg = total / len(numbers)

print("Сумма:", total)
print("Максимум:", maximum)
print("Минимум:", minimum)
print("Среднее:", avg)