def born_cat(count_cat):
    if count_cat >= 2:
        count_cat += 6
        return count_cat


def count_legs(callback, num):
    count_cat = callback(num)
    count_cat_legs = count_cat * 4
    print(count_cat_legs)


count_legs(born_cat, 2)
