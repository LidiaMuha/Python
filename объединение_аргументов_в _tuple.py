def sum_nums(*args):  # в функции числа конвертируются в кортеж из-за опратора *
    print(args)
    print(type(args))
    print(args[0])
    # используем встроенную функцию для суммирования элементов кортежа
    return sum(args)


print(sum_nums(2, 3, 7))  # вводим аргументы - это обычные числа


# ------------------------
def get_posts_info(name, post_id):
    info = f"{name} wrote {post_id} posts"
    return info


info = get_posts_info(post_id=93, name='Lidia')
print(info)
# Но можно добавить ключевые слова и порядок аргуменетов станет неважен
