n = input("Enter number: ")

while n < '0':
    print("Try again. The number should be greater than 0")
    n = input('Enter a number greater than 0: ')

print(f"({n} + {n + n} + {n + n + n}) = {int(n) + int(n + n) + int(n + n + n)}")
