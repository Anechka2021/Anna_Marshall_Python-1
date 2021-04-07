my_list = [9, 8, 7, 7, 6, 6, 5, 5, 3, 3, 2, 2, 1]
new_number = int(input("Enter a new element of rating as a whole number: "))
i = 0
for n in my_list:
    if new_number <= n:
        i += 1
my_list.insert(i, new_number)
print(my_list)
