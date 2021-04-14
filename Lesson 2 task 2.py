  my_list = input("Insert numbers of the list with space: ").split()
  print('The list: ', my_list)

  idx = len(my_list) if len(my_list} % 2 ==0 else len(my - list) - 1

  my_list[:indx:2], my_list[1:idx:2] = my_list[1:idx:2], my_list[:idx:2]
  print('The changed list: ', my_list)