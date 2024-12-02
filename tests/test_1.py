from datetime import time

def test_dark_theme_by_time():

    current_time = time(hour=23)

    if time(hour=22) <= current_time or current_time < time(hour=6):
        return True
    else:
        return False

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():

    current_time = time(hour=16)
    dark_theme_enabled_by_user = True

    if dark_theme_enabled_by_user:
        if time(hour=22) <= current_time or current_time < time(hour=6):
            return True
        else:
            return False
    elif dark_theme_enabled_by_user:
        return True
    else:
        return False

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]
    for user in users:
        if user['name'] == 'Olga':
            return user

    suitable_users = user

    assert suitable_users == {"name": "Olga", "age": 45}

    suitable_users = []
    for user in users:
        if users ['age'] < 20:
            suitable_users.append(user)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = open_browser

    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = go_to_companyname_homepage
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = find_registration_button_on_login_page
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"

def print_function_and_args(func, *args):
    func_name = func.__name__.replace('_', ' ').title()
    arg_names = ', '.join([*args])
    print(f"{func_name} [{arg_names}]")
    return f"{func_name} [{arg_names}]"