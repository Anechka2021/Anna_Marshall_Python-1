def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        div_num = s_1 / s_2
    except ZeroDivisionerror:
        return "No / 0"
    except ValueError:
        return 'No value'
    return round(div_num, 3)

print(div(input("Please enter your first number: "), input("Please enter your second number: ")))