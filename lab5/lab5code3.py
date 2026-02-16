num = []
l = int(input("Введите кол-во чисел которые вы хотите доавить: "))


pos = 0
neg = 0
sred = 0

for i in range(l):
    n = int(input("Введите числа: "))
    num.append(n)

for f in range(len(num)):
    if num[f] > 0:
        pos += 1
    if num[f] <0:
        neg += 1
    if num[f] % 2 == 0:
        sred += 1

print(pos)
print(neg)
print(sred)
