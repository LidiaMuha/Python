def get_posts_info(**person):
    print(person)
    print(type(person))
    # мы обращаемся к значениям ключей словаря и вставляем их значения в строку
    info = (
        f"{person['name']} wrote "
        f"{person['post_id']} posts"
    )
    return info


info = get_posts_info(name='Lidia', post_id=93)
print(info)
