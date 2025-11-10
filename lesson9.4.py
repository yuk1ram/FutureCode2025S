from random import randint

x = randint(1000, 10000)
x = str(x)

i = 10
while i > 0:
    n = input("введите ваш код")
    if n == x:
        print('код угадан')
    for ii in range(0,4):
        if n[ii] == x[ii]:
           print("совпадение по", ii, "числу")