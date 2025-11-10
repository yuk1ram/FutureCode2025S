count = 0

n = int(input())
for i in range (10, n):
    if i % 6 == 0 and (i % 10 == 4 or i % 10 == 8):
        count += 1

print(count)