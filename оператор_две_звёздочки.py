button = {
    'width': 200,
    'text': 'Buy'
}


red_button = {
    **button,
    'color': 'red'
}

print(red_button)  # {'width': 200, 'text': 'Buy', 'color': 'red'}

print(button)  # {'width': 200, 'text': 'Buy'}

print('---------------------------')

button_info = {
    'text': 'Buy'
}

button_sryle = {
    'color': 'yellow',
    'widfh': 200,
    'height': 300
}

button = {
    **button_info,
    **button_sryle
}

button_2 = button_info | button_sryle

print(button)
print(button_2)


print('---------------------------')


button_default = {
    'text': 'Ok',
    'color': 'black',
    'widfh': 0,
    'height': 0
}

button_sryle = {
    'color': 'yellow',
    'widfh': 200,
    'height': 300
}

button_3 = button_info | button_sryle

# {'text': 'Buy', 'color': 'yellow', 'widfh': 200, 'height': 300}
print(button_3)
