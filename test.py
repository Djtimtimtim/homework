import json

# Создаем объект
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Сериализуем объект в строку JSON
json_string = json.dumps(data)
print(json_string)
