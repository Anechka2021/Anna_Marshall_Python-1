name = input("Enter your name: ")
surname = input("Enter your surname: ")
year = int(input("Enter your date of birth: "))
city = input("Enter city where you live: ")
email = input("Enter your email: ")
phone_number = input("Enter your phone number: ")

def my_func (name, surname, year, city, email, phone_number):
     return ' '.join([name, surname, year, city, email, phone_number])
print(my_func(surname = 'Marshall', name = 'Anna', year = '1981', city = 'Edinburgh', email = 'error@mail.ru', phone_number = '07920013359'))


