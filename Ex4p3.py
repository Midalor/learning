b = int(input("Введите большее значение: "))
a = int(input("Введите меньшее значение: "))
x = 0
if b < a:
    print("Не верное значение.")
else:
    while a <= b:
        if b % 2 == 0:
            x = x+1
            b= b - 1
        else:
            b= b - 1
    print ("количество целых числе:", x)