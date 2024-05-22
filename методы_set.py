photo_sezes = {'1920x1080', '800x600'}
photo_sezes.add('1024x768')
print(photo_sezes)

other_sizes = {'500x100', '800x600'}

all_sizes = photo_sezes.union(other_sizes)
print(all_sizes)

commoms_s = photo_sezes.intersection(other_sizes)
print(commoms_s)  # пересечение наборов

# входит ли одно множество в другое
nums = {10, 5, 35}
other_nums = {20, 5, 12, 10, 35}

res = nums.issubset(other_nums)
print(res)

# является ли множество супермножетсвом по отношению к другому множетсу
res_2 = other_nums.issuperset(nums)
print(res_2)
