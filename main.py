# 1
value1 = input("Введите двухзначное число: ")
print(value1[0],value1[1], sep="\n")

# 2
value2 = input("Введите трехзначное число: ")
print(value2[0],value2[1],value2[2], int(value2[0])+int(value2[1])+int(value2[2]), sep="\n")

# 3
value3 = input("Введите первое число: ")
value4 = input("Введите второе число: ")
print(value3,value4,sep="")

# 4
value5 = int(input("Введите температуру по шкале Цельсия: "))
farengeit = 9/5*value5+32
print(value5, "по шкале Цельсия, это", farengeit, "по Фаренгейту")