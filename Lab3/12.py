class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def total_salary(self):
        return float(self.base_salary)

class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent

    def total_salary(self):
        # Формула для менеджера
        return self.base_salary * (1 + self.bonus_percent / 100)

class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = completed_projects

    def total_salary(self):
        # Формула для разработчика
        return self.base_salary + (self.completed_projects * 500)

class Intern(Employee):
    # У стажера нет бонусов, метод total_salary наследуется от Employee
    pass

# --- Логика обработки ввода ---

try:
    line = input().split()
    if not line:
        exit()

    role = line[0]
    name = line[1]
    base_salary = int(line[2])

    # Создаем нужный объект в зависимости от роли
    if role == "Manager" or role == "Менеджер":
        bonus = int(line[3])
        emp = Manager(name, base_salary, bonus)
    elif role == "Developer" or role == "Разработчик":
        projects = int(line[3])
        emp = Developer(name, base_salary, projects)
    elif role == "Intern" or role == "Стажер":
        emp = Intern(name, base_salary)
    
    # Вывод в требуемом формате
    print(f"Name: {emp.name}, Total: {emp.total_salary():.2f}")

except (EOFError, IndexError):
    pass