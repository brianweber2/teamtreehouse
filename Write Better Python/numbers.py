my_list = [5, 2, 1, True, "abcdefg", 3, False, 4]

for items in my_list:
    if isinstance(my_list, str):
        my_list.remove(items)
    else:
        print(items)
