user_data = ['Lidia', 23]


def user_info(name, comments_qty):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"


print(user_info(*user_data))


# или мы можем написать после бъявления функции
# распаковка списка
# my_name, my_comments = user_data
# print(user_info(my_name, my_comments))
