import random


def get_user_choice():
    while True:
        user_choice = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()
        if user_choice in ["камень", "ножницы", "бумага"]:
            return user_choice
        else:
            print("Некорректный ввод! Пожалуйста, введите 'камень', 'ножницы' или 'бумага'.")


def get_computer_choice():
    return random.choice(["камень", "ножницы", "бумага"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"

    if (user_choice == "камень" and computer_choice == "ножницы") or \
            (user_choice == "ножницы" and computer_choice == "бумага") or \
            (user_choice == "бумага" and computer_choice == "камень"):
        return "Вы победили!"
    else:
        return "Компьютер победил!"


def play_game():
    print("Добро пожаловать в игру 'Камень-Ножницы-Бумага'!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Ваш выбор: {user_choice}")
        print(f"Выбор компьютера: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
        if play_again != "да":
            print("Спасибо за игру!")
            break


play_game()
