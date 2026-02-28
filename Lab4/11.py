import sys
import json
import copy

def apply_patch(source, patch):
    """
    Рекурсивно применяет патч к исходному JSON-объекту.
    """
    if isinstance(source, dict) and isinstance(patch, dict):
        # Создаём глубокую копию исходного объекта, чтобы не изменять его
        result = copy.deepcopy(source)
        for key, pval in patch.items():
            if pval is None:
                # Удаляем ключ, если он существует
                result.pop(key, None)
            else:
                if key in result and isinstance(result[key], dict) and isinstance(pval, dict):
                    # Рекурсивно обновляем вложенный объект
                    result[key] = apply_patch(result[key], pval)
                else:
                    # Замена или добавление значения
                    result[key] = pval
        return result
    else:
        # Нестандартная ситуация – просто возвращаем патч
        return patch

def main():
    # Читаем две строки ввода
    data = sys.stdin.read().strip().splitlines()
    if len(data) < 2:
        return

    source_str, patch_str = data[0].strip(), data[1].strip()
    try:
        source = json.loads(source_str)
        patch = json.loads(patch_str)
    except json.JSONDecodeError:
        sys.stderr.write("Invalid JSON input")
        return

    result = apply_patch(source, patch)

    # Выводим результат в компактной форме с сортировкой ключей
    json.dump(result, sys.stdout, separators=(',', ':'), sort_keys=True)

if __name__ == "__main__":
    main()