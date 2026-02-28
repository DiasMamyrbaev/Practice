import sys
import json

def serialize(val):
    """
    Возвращает компактное JSON-представление значения.
    Для отсутствующей стороны используется '<missing>' без кавычек.
    """
    if val is ...:  # не используется, но для полноты
        return 'null'
    return json.dumps(val, separators=(',', ':'), sort_keys=True)

def compare(a, b, path, diffs):
    """
    Рекурсивно сравнивает два JSON-объекта (словаря) и заполняет список diffs
    кортежами (путь, старое_значение, новое_значение).
    """
    keys = set(a.keys()) | set(b.keys())
    for key in keys:
        current_path = '.'.join(path + [key])
        if key in a and key in b:
            aval = a[key]
            bval = b[key]
            if isinstance(aval, dict) and isinstance(bval, dict):
                # оба значения — объекты, рекурсивно спускаемся
                compare(aval, bval, path + [key], diffs)
            else:
                # иначе сравниваем как есть
                if aval != bval:
                    diffs.append((current_path, serialize(aval), serialize(bval)))
        elif key in a:
            # ключ есть только в A
            diffs.append((current_path, serialize(a[key]), '<missing>'))
        else:
            # ключ есть только в B
            diffs.append((current_path, '<missing>', serialize(b[key])))

def main():
    data = sys.stdin.read().strip().splitlines()
    # пропускаем пустые строки
    lines = [line.strip() for line in data if line.strip()]
    if len(lines) < 2:
        return

    try:
        a = json.loads(lines[0])
        b = json.loads(lines[1])
    except json.JSONDecodeError:
        sys.stderr.write("Invalid JSON input")
        return

    diffs = []
    compare(a, b, [], diffs)

    if not diffs:
        print("No differences")
    else:
        diffs.sort(key=lambda x: x[0])  # сортировка по пути
        for path, old, new in diffs:
            print(f"{path} : {old} -> {new}")

if __name__ == "__main__":
    main()