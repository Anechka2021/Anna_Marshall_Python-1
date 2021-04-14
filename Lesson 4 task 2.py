my_list = [16, 2, 4, 6, 8, 5, 10]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num-1] < my_list[num]]
print(f'Original list {my_list}')
print(f'New list {my_new_list}')
