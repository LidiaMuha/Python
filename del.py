my_list = [1, 2]

# print(del my_list[0])
# Ответ: SyntaxError: invalid syntax
# это значит, что del - инструкция

del my_list[0]
my_list.__delitem__(0)
print(my_list)
