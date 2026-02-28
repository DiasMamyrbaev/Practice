import importlib
import sys

def solve():
    # Читаем количество запросов
    line = sys.stdin.readline()
    if not line:
        return
    q = int(line.strip())

    for _ in range(q):
        query = sys.stdin.readline().split()
        if not query:
            continue
        
        module_path = query[0]
        attr_name = query[1]

        try:
            # Пытаемся импортировать модуль
            module = importlib.import_module(module_path)
            
            try:
                # Пытаемся получить атрибут
                attribute = getattr(module, attr_name)
                
                # Проверяем, является ли объект вызываемым (функция, класс и т.д.)
                if callable(attribute):
                    print("CALLABLE")
                else:
                    print("VALUE")
                    
            except AttributeError:
                print("ATTRIBUTE_NOT_FOUND")
                
        except ModuleNotFoundError:
            print("MODULE_NOT_FOUND")
        except Exception:
            # На случай специфических ошибок при импорте некоторых системных модулей
            print("MODULE_NOT_FOUND")

if __name__ == "__main__":
    solve()