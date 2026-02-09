#огород
n = int(input("Длинна огорода :"))
m = int(input("Ширина огорода :"))

count_c = 0
count_t = 0
count_p = 0
count_dot = 0

for i in range(n):
    for j in range(m):
        x = i + j

        if x % 12 == 0:
           print('P', end=" ")
           count_p += 1

        elif x % 3 == 0:
            print("C",end=" ")
            count_c += 1

        elif x % 4 == 0:
            print("T",end=" ")
            count_t += 1

        else:
            print(".",end=" ")
            count_dot += 1

    print()


print("Картошка (P):",count_p)
print("Морковь (C):",count_c)
print("Помидор (T):",count_t)
print("Пустота (.):",count_dot)

#Смысл кода-создать наглядную таблицу огорода с разными овощами,показать их распределение и подсчитать количество каждого типа,используя циклы и условия

