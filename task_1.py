# Лабораторная №1: Первичная инициализация
# Курс: Основы теории систем
# Студент: Яруллин Руслан Харисович

def get_system_info():
    """
    Эта функция должна вернуть словарь с информацией о вашей "системе".
    """
    # TODO: Заполните словарь вашими реальными данными
    system_info = {
        "student_name": "Яруллин Руслан Харисович",
        "academic_group": "ИВТИИбд-12",
        "github_link": "https://github.com/rheinstd"
    }
    return system_info

# Вывод информации для проверки
if __name__ == "__main__":
    info = get_system_info()
    print("Лабораторная работа №1")
    print("Информация о системе:")
    for key, value in info.items():
        print(f"- {key}: {value}")
