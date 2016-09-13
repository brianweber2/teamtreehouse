my_list = [5, 2, 1, True, "abcdefg", 3, False, 4]

del my_list[3]  # my_list = [5, 2, 1, "abcdefg", 3, False, 4]
del my_list[3]  # my_list = [5, 2, 1, 3, False, 4]
del my_list[4]  # my_list = [5, 2, 1, 3, 4]
print(my_list)