score = int(input("Введите число от 1 до 100:"))

if score >= 1 and score <= 60 :
    print("Ваша оценка D")

elif score >= 60 and score <= 74 :
    print("Ваша оценка C")

elif score >= 75 and score <= 89 :
    print("Ваша оценка B")

elif score >= 90 and score <= 100 :
    print("Ваша оценка A")

else:
    print("Вы ввели недопустимое число")
