# Задача №1
# Должен получится следующий словарь

# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }
import pprint
import json

def read_cookbook(file_path):
    # Открываем файл для чтения с кодировкой UTF-8
    with open(file_path, 'r', encoding='utf-8') as file:
        cook_book = {}
        while True:
            # Читаем название блюда
            dish_name = file.readline().strip()
            if not dish_name:
                break  # Если название блюда пустое, выходим из цикла
            # Читаем количество ингредиентов для текущего блюда
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                # Читаем строку с ингредиентом и разбиваем её на части
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                # Добавляем ингредиент в список
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            # Добавляем блюдо и его ингредиенты в кулинарную книгу
            cook_book[dish_name] = ingredients
            file.readline()  # Пропускаем пустую строку между рецептами
    return cook_book

def save_cookbook(cook_book, output_file_path):
    # Сохраняем словарь в файл в формате JSON
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(cook_book, file, ensure_ascii=False, indent=4)

# Пример использования
file_path = './recipes.txt'
output_file_path = './cook_book.json'
cook_book = read_cookbook(file_path)
# Форматированный вывод кулинарной книги
pprint.pprint(cook_book)
# Сохранение кулинарной книги в файл
save_cookbook(cook_book, output_file_path)

