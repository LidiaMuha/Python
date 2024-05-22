list_post_theme = [{'sience': 'Bioligy', 'description': 'life'}, {
    'sience': 'History', 'description': 'remember'}, {'sience': 'Mathematics', 'description': 'clever'}]


def post_theme(sience, description):
    return f"секция с темами постов: {sience}, описание темы - {description}"


dict_one, dict_two, dict_three = list_post_theme

print(post_theme(**dict_one))
print(post_theme(**dict_two))
print(post_theme(**dict_three))
