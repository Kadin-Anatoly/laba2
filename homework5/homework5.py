import random


def find_multiples_of_x():
    while True:
        try:
            x = int(input("Введите цифру X (от 1 до 9): "))
            if x < 1 or x > 9:
                raise ValueError("Цифра должна быть от 1 до 9.")
            numbers = [random.randint(0, 200) for _ in range(10)]
            print(f"Сгенерированные числа: {numbers}")
            multiples_of_x = list(filter(lambda num: num % x == 0, numbers))
            if multiples_of_x:
                print(f"Числа, кратные {x}: {multiples_of_x}")
            else:
                print(f"Нет чисел, кратных {x}.")
            break

        except ValueError as e:
            print(f"Ошибка: {e}. Пожалуйста, введите правильное значение.")


find_multiples_of_x()
