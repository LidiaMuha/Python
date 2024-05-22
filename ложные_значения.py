print(bool(0))
print(bool(''))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(set()))
print(bool(range(0)))

# False
# False
# False
# False
# False
# False
# False


print(not not 'abc')  # True, так как not конвертирует в логический тип


my_list = [1, 2]

if len(my_list) > 0:
    print("В этом списке есть элементы")


# идентично
if my_list:
    print("В этом списке есть элементы")

print(bool(my_list))
