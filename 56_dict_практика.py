# my_list = [0, True, 'abc']
# my_dict = dict(my_list)  # TypeError


new_list = [['first', 0], ['second', True]]
new_dict = dict(new_list)
print(new_dict)  # {'first': 0, 'second': True}
