import random
rows = int(input("Введите кол-во строк: "))
cols= int(input("Введите кол-во столбцов: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = random.randint(1, 20)
        row.append(value)
    matrix.append(row)
print("\nМатрица:")

for row in matrix:
    for value in row:
        print(f"{value:4}", end="")
    print()