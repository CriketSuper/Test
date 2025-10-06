import random

import string
def generate_random_string(length: int) -> str:
    """Генерирует случайную строку из букв ASCII и цифр."""

    # Определяем набор символов, из которых будет состоять строка
    characters = string.ascii_letters + string.digits + string.punctuation + ' '

    # Генерируем строку
    random_string = ''.join(random.choice(characters) for i in range(length))

    return random_string

# Пример использования

msg = input('Введите сообщение: ')
n = int(input('Введите число: '))

final_text = ''.join(let + generate_random_string(n) for let in msg)

print(final_text)