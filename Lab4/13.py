import sys
import json

class NotFound(Exception):
    """Исключение, сигнализирующее о том, что путь не найден."""
    pass

def navigate(data, path):
    """
    Проходит по пути path в структуре data.
    Путь разбивается точками. Каждая часть может быть:
    - ключом объекта (например, "user")
    - ключом с индексами (например, "friends[0]")
    - сразу индексами (например, "[0]")
    Поддерживаются множественные индексы (например, "a[0][1]").
    Возвращает найденное значение или бросает NotFound.
    """
    parts = path.split('.')
    current = data
    for part in parts:
        if part.startswith('['):
            # Часть начинается с индекса — применяем индексы к текущему значению
            rest = part
            while rest:
                if not rest.startswith('['):
                    raise NotFound
                close = rest.find(']')
                if close == -1:
                    raise NotFound
                try:
                    index = int(rest[1:close])
                except ValueError:
                    raise NotFound
                if not isinstance(current, list):
                    raise NotFound
                if index < 0 or index >= len(current):
                    raise NotFound
                current = current[index]
                rest = rest[close+1:]   # убираем обработанный индекс
        else:
            # Часть содержит ключ, возможно с индексами
            if '[' in part:
                # Разделяем на ключ и индексы
                idx = part.find('[')
                key = part[:idx]
                # Применяем ключ
                if not isinstance(current, dict) or key not in current:
                    raise NotFound
                current = current[key]
                # Обрабатываем индексы
                rest = part[idx:]
                while rest:
                    if not rest.startswith('['):
                        raise NotFound
                    close = rest.find(']')
                    if close == -1:
                        raise NotFound
                    try:
                        index = int(rest[1:close])
                    except ValueError:
                        raise NotFound
                    if not isinstance(current, list):
                        raise NotFound
                    if index < 0 or index >= len(current):
                        raise NotFound
                    current = current[index]
                    rest = rest[close+1:]
            else:
                # Простой ключ без индексов
                if not isinstance(current, dict) or part not in current:
                    raise NotFound
                current = current[part]
    return current

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return

    # Первая строка – JSON
    json_str = data[0].strip()
    try:
        obj = json.loads(json_str)
    except json.JSONDecodeError:
        sys.stderr.write("Invalid JSON")
        return

    # Вторая строка – количество запросов
    if len(data) < 2:
        return
    try:
        q = int(data[1].strip())
    except ValueError:
        return

    # Остальные строки – сами запросы
    queries = [line.strip() for line in data[2:2+q]]

    for query in queries:
        try:
            result = navigate(obj, query)
            print(json.dumps(result, separators=(',', ':')))
        except NotFound:
            print("NOT_FOUND")

if __name__ == "__main__":
    main()