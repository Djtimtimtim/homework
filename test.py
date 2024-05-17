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

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                if name in shop_list:
                    shop_list[name]['quantity'] += ingredient['quantity'] * person_count
                else:
                    shop_list[name] = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count
                    }
    return shop_list

# Пример использования
file_path = './cookbook/recipes.txt'
output_file_path = './cookbook/cook_book.json'
cook_book = read_cookbook(file_path)
# Форматированный вывод кулинарной книги
# Сохранение кулинарной книги в файл
save_cookbook(cook_book, output_file_path)

# Получение списка покупок
shop_list = get_shop_list_by_dishes(cook_book, ['Запеченный картофель', 'Омлет'], 2)
pprint.pprint(shop_list)
