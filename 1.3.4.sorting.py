s = [13, 25, 3, 18, 12, 11, 2, 29, 24, 12, 31, 24, 22, 6, 11,
29, 16, 29, 25, 22, 13, 14, 24, 16]
sum_chet = 0
sum_nechet = 0
for i in s:
    if i % 2 == 0:
        sum_chet += 1
    else:
     sum_nechet += 1
if sum_chet > sum_nechet:
    print('Выиграли четные')
else:
    print('Выиграли нечетные')