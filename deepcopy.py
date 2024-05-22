from copy import deepcopy

info = {
    'name': 'Lida',
    'is_instructor': False,
    'review': []
}

info_deepcopy = deepcopy(info)

# Два варианта дополнения
info_deepcopy['review'].append('Good')
# info_deepcopy['review'] = 'Good'

# НО если мы хотим ИМЕННО добавить навое значение без стирания старого
# то используем append
info_deepcopy['review'].append('Very good')

print(info)
print(info_deepcopy)
