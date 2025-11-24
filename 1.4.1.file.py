with open('data.txt', 'rw', encoding='utf-8') as file:
    file.write("\n4444444444")
    file.write("\n555555555")

file = open('data.txt', 'r')
print(file.read())


