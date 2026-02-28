import json

# Чтение из строки
json_str = '{"name": "Aida", "age": 25}'
data = json.loads(json_str)
print(data["name"])

# Python -> JSON
person = {"name": "Dias", "age": 18, "city": "Almaty"}
json_output = json.dumps(person, indent=4)
print(json_output)

# Чтение из файла sample-data.json
with open("sample-data.json", "r", encoding="utf-8") as f:
    sample_data = json.load(f)
print(sample_data.keys())

# Обработка (например, если это список словарей)
if isinstance(sample_data, list):
    for item in sample_data:
        print(item.get("name", "No name"))

# Запись в новый файл
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(sample_data, f, indent=2, ensure_ascii=False)