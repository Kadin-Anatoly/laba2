def get_number():
    for num in range(30):
        if num % 2 != 0:
            yield num


generator = get_number()

first = fifth = last = None
count = 0

for num in generator:
    count += 1
    if count == 1:
        first = num
    if count == 5:
        fifth = num
    last = num

print(f"Первое значение: {first}")
print(f"Пятое значение: {fifth}")
print(f"Последнее значение: {last}")
