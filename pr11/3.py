import os
import re

def rename_files(current_format, expected_format):
    # Отримання списку файлів у поточній директорії
    files = os.listdir()

    for file in files:
        if file.endswith('.mp3'):  # Перевірка, чи файл є музичним
            match = re.match(current_format, file)  # Пошук відповідності формату
            if match:
                groups = match.groups()
                new_name = expected_format.format(*groups) + '.mp3'  # Форматування нового імені
                print(f"{file} -> {new_name}")

                # Створення необхідних директорій, якщо вони не існують
                directory = os.path.dirname(new_name)
                if not os.path.exists(directory):
                    os.makedirs(directory)

                # Перейменування файлу
                os.rename(file, new_name)

# Задані формати файлів
current_file_format = r'(.+) - (\d+) (.+) \((\d+)\).mp3'
expected_file_format = '{0}/{3} {0}/{1} {2}'

# Виклик функції перейменування файлів
rename_files(current_file_format, expected_file_format)
