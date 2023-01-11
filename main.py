from random import randint


def attack(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс противнику урон, равный '
                f'{5 + randint(-3, -1)}')
    return None


def defence(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return None


def special(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        return (f'{char_name} применил умение «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил умение «Защита {10 + 30}»')
    return None


def start_training(char_name: str, char_class: str) -> str:
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи команду:')
    print('attack-атаковать, defence-блокировать, special-суперсила.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    approve_choice: str = None
    char_class: str = None
    while approve_choice != 'y':
        char_class = input(
            'Введи имя: Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель. Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг. Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь. Черпает силы из природы, веры и духов.')
        approve_choice = input(
            'Нажми(Y), чтобы подтвердить,'
            'или другую для выбора другого персонажа').lower()
    return char_class


def main() -> str:
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
    return None
