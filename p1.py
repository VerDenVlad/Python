# Угадай число
import random

rand_num = random.randint(1, 5)
user_num = input("Угадай число (от 1 до 5):")

if user_num == rand_num:
    print("Вы угадали!")
else:
    print("Вы не угадали :()")
    print(f"Было загадано число {rand_num}")