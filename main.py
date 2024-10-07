import random

secret_number = random.randint(1, 10)
attempts = 3

print("Угадайте число от 1 до 10. У вас 3 попытки.")

for attempt in range(attempts):
    guess = int(input("Введите число: "))

    if guess == secret_number:
        print("Поздравляю! Вы угадали число!")
        break
    else:
        print("Неправильно. Попробуйте еще раз.")
else:
    print(f"Вы исчерпали все попытки. Загаданное число было: {secret_number}")



