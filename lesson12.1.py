health = int(input('введите уровень здоровья: '))

if health >= 90:
    print('персонаж здоров')
elif 70 <= health < 90:
    print('персонажу нужно выпить зелье. согласны? (Y / N)')
    answer = input()
    if answer.lower() == 'y':
        health += 10
        print('здоровье увеличено до ', health)
elif 30 <= health < 70:
        print('вы ранены. использовать аптечку? (Y / N)')
        answer = input()
        if answer.lower() == 'y':
            health += 30
            print('здоровье увеличено до ', health)

