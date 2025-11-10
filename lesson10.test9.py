number = 384
sum_digits = 0
for digit in str(number):
    sum_digits = sum_digits + int(digit)
if sum_digits % 2 == 0:
    result = sum_digits * 2
else:
    result = sum_digits + 1
print(result)