def sal():
    try:
        time = float(input('Enter time in hours '))
        salary = int(input('Payment per hour in £ '))
        bonus = int(input('Bonus in £ '))
        res = time * salary + bonus
        print(f'Total payment to the employee in £ is: {res}')
    except ValueError:
        return print('Not a number')
sal()