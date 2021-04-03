
num_int = int(input("Enter a positive number: "))
greatest_dig = 0
num = num_int

while num > 0:
    digit = num % 10
    if digit > greatest_dig:
        greatest_dig = digit
        if greatest_dig == 10:
            break
        num = num // 10

    print(f"The greatest digit in the number is {num_int} equals {greatest_dig}")
