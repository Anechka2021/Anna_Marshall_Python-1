month = int(input("Insert a month of a year from 1 to 12: "))

month_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if month in month_dict:
    print(f"{month} month of the year - {month_dict[month]}")
    print(f"{month} month of the year -  {month_list[month-1]}")
    else:
         print("Wrong number. Try again.")
