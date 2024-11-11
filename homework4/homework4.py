from datetime import datetime


def get_months_suffix(months):
    if 11 <= months % 100 <= 14:
        return "месяцев"
    elif months % 10 == 1:
        return "месяц"
    elif 2 <= months % 10 <= 4:
        return "месяца"
    else:
        return "месяцев"


def get_age_suffix(age):
    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"


def calculate_age():
    while True:
        try:
            birth_date_input = input("Введите вашу дату рождения в формате день/месяц/год (например, 25/12/2000): ")
            birth_date = datetime.strptime(birth_date_input, "%d/%m/%Y")
            today = datetime.today()
            if birth_date > today:
                raise ValueError("Дата рождения не может быть в будущем.")

            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            if age < 1:
                months = (today.month - birth_date.month) + 12 * (today.year - birth_date.year)
                if today.day < birth_date.day:
                    months -= 1
                print(f"Вам {months} {get_months_suffix(months)}.")
            else:
                age_suffix = get_age_suffix(age)
                print(f"Ваш возраст: {age} {age_suffix}.")
            break
        except ValueError as e:
            print(f"Ошибка: {e}. Пожалуйста, введите дату в правильном формате.")


calculate_age()
