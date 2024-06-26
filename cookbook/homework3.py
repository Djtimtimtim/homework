#Задача №3
# В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны, пример для выполнения домашней работы можно взять тут

# Необходимо объединить их в один по следующим правилам:

# Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
# Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем

# Пример
# Даны файлы: 1.txt

# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1

# 2.txt

# Строка номер 1 файла номер 2

# Итоговый файл:

# 2.txt
# 1
# Строка номер 1 файла номер 2

# 1.txt
# 2
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1

import os  # Импорт модуля os для работы с файловой системой

# Укажите путь к папке с файлами
folder_path = './text'
output_file = './filtered_text'

# Получаем список файлов в папке
files = []
for f in os.listdir(folder_path):  # Получаем список всех файлов и папок в указанной директории
    if os.path.isfile(os.path.join(folder_path, f)):  # Проверяем, является ли элемент файлом
        files.append(f)  # Добавляем файл в список

# Создаем список для хранения информации о файлах
file_info = []

# Считываем содержимое каждого файла и сохраняем информацию о нем
for file in files:
    with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:  # Открываем файл в режиме чтения
        lines = f.readlines()  # Читаем все строки файла
        file_info.append((file, len(lines), lines))  # Сохраняем имя файла, количество строк и содержимое

# Определяем функцию для получения количества строк
def get_line_count(file_info_item):
    return file_info_item[1]  # Возвращаем количество строк

# Сортируем файлы по количеству строк
file_info = sorted(file_info, key=get_line_count)  # Сортируем список по количеству строк

# Записываем содержимое в итоговый файл
with open(output_file, 'w', encoding='utf-8') as f:  # Открываем итоговый файл в режиме записи
    for info in file_info:
        f.write(f"{info[0]}\n{info[1]}\n")  # Записываем имя файла и количество строк
        f.writelines(info[2])  # Записываем содержимое файла

print(f"Файлы объедены в {output_file}")


# os.listdir(path):
# Возвращает список файлов и папок в указанной директории path.

# os.path.isfile(path):
# Проверяет, является ли указанный путь path файлом.

# os.path.join(path, *paths):
# Объединяет один или несколько компонентов пути в один путь.

# open(file, mode, encoding):
# Открывает файл file в указанном режиме mode с заданной кодировкой encoding. В данном случае используется режим чтения 'r' и кодировка 'utf-8'.

# file.readlines():
# Читает все строки из файла и возвращает их в виде списка.

# sorted(iterable, key):
# Возвращает отсортированный список из элементов iterable на основе функции ключа key. В данном случае используется функция get_line_count для сортировки по количеству строк.

# file.write(string):
# Записывает строку string в файл.

# file.writelines(lines):
# Записывает список строк lines в файл.

# print(object):
# Выводит объект object на стандартный вывод.
