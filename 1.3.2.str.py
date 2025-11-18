text_list = input().split()
cesar_list =[]

for word in text_list:
    middle = len(word)//2
    cesar_list.append(word[middle:]+word[0:middle])

print(text_list)
