from random import randint

x = randint(1000, 10000)
is_guess = False

while not is_guess:
    n = int(input("введите ваш код"))
    if n==x:
        print("сундук открыт! сокровища ваши!")
        is_guess = True
    elif n == 0:
        is_guess = True
        print("код-", x)
    else:
        print("код не подошел... попробуйте еще раз!")