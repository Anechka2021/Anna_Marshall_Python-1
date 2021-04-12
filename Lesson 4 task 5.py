def sum_num():
    s = 0
    while True:
        in_list = input("Enter any number, enter 'Q' to exit: ").split()
        for num in in_list:
            if num == 'Q':
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print("Enter 'Q' to exit the programme.")
                print(f"Sum of all numbers = {s}")
print(sum_num())

