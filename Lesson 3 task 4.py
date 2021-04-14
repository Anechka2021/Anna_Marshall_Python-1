def my_pow_fun(x, y):
    try:
        res = x ** y
    except TypeError:
        return "Enter a number and a number in a negative power: "
    return res
print(my_pow_fun(3.4, -4))

