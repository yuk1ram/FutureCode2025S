text = input("введите строку для проверки палиндрома")

text = text.lower()
text = text.replace(' ', '')

reverse_text = text[::-1]

if reverse_text == text:
    print("палиндром")
else:
    print ("не палиндром")
