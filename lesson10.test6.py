count = 0
for i in range (10, 100):
    if i % 6 == 0 and (i % 10 == 2 or i % 10 == 8):
        count += 1

print(count)