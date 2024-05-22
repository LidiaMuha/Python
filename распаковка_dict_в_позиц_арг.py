user_profile = {
    'name': 'Lidia',
    'comments_qty': 23
}


def user_info(name, comments_qty=0):  # comments_qty=0 - это дефолтное значение при отсутствии
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"


# в качестве аргумента передаём распакованный словарь
print(user_info(**user_profile))
