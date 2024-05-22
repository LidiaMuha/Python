def othet_fn():
    pass


def fn_with_callback(callback_fn):
    callback_fn()


# в аргументе функция НЕ вызывается, а указывается, как аргумент
fn_with_callback(othet_fn)

print('------------------------------------------------------')


def print_number_info(num):
    if (num % 2) == 0:
        print("Введённое число чётное")
    else:
        print("Введённое число нечётное")


def print_square_num(num):
    print("Результатом возвреденя в квадрат данного числа:", num * num)


def process_number(num, callback_fn):
    callback_fn(num)


entered_num = int(input("Введите число: "))

process_number(entered_num, print_number_info)
process_number(entered_num, print_square_num)


print('------------------------------------------------------')

# Метод, который отсылает данные на сервер (условно, не реализовано)


def send_data(data):
    # как-то отсылает данные
    pass

# Метод, который изменяет данные (условно, не реализовано)


def process_date(input_data, send_data_fn):
    update_data = input_data.copy()
    # как-то изменяет данные
    send_data_fn(update_data)


process_date({'name': 'Lidia'}, send_data)
